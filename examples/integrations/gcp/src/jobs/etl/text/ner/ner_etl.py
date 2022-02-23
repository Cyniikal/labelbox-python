import random
import json
import argparse
import time
import logging
from concurrent.futures import ThreadPoolExecutor
import os

from google.cloud import storage
from google.cloud import secretmanager

from labelbox import Client
from labelbox import Project
from labelbox.data.annotation_types import TextEntity
from labelbox.data.annotation_types import Label

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

VERTEX_MIN_TRAINING_EXAMPLES, VERTEX_MAX_TRAINING_EXAMPLES = 50, 100_000
MIN_ANNOTATIONS, MAX_ANNOTATIONS = 1, 20
MIN_ANNOTATION_NAME_LENGTH, MAX_ANNOTATION_NAME_LENGTH = 2, 30

# Optionally set env var for testing
_labelbox_api_key = os.environ.get('LABELBOX_API_KEY')
if _labelbox_api_key is None:
    client = secretmanager.SecretManagerServiceClient()
    secret_id = "labelbox_api_key"
    name = f"projects/{os.environ['GOOGLE_PROJECT']}/secrets/{secret_id}/versions/1"
    response = client.access_secret_version(request={"name": name})
    _labelbox_api_key = response.payload.data.decode("UTF-8")


def process_label(label: Label) -> str:
    text_annotations = []
    for annotation in label.annotations:
        if isinstance(annotation.value, TextEntity):
            entity = annotation.value
            # TODO: Check this condition up front by looking at the ontology
            if len(annotation.name) < MIN_ANNOTATION_NAME_LENGTH or len(
                    annotation.name) > MAX_ANNOTATION_NAME_LENGTH:
                logger.info(
                    "Skipping annotation `{annotation.name}`. "
                    "Lenght of name invalid. Must be: "
                    f"{MIN_ANNOTATION_NAME_LENGTH}<=num chars<={MAX_ANNOTATION_NAME_LENGTH}"
                )
                continue

            text_annotations.append({
                "startOffset": entity.start,
                "endOffset": entity.end + 1,
                "displayName": annotation.name
            })

    # TODO: You can use a label to annotate between 1 and 10 words.
    # Verify ^^ is what we are checking for
    if not (MIN_ANNOTATIONS <= len(text_annotations) <= MAX_ANNOTATIONS):
        logger.info("Skipping label. Number of annotations is not in range: "
                    f"{MIN_ANNOTATIONS}<=num annotations<={MAX_ANNOTATIONS}")
        return

    return json.dumps({
        "textSegmentAnnotations": text_annotations,
        # Note that this always uploads the text data in-line
        "textContent": label.data.value,
        'dataItemResourceLabels': {
            "aiplatform.googleapis.com/ml_use": ['test', 'train', 'validation']
                                                [random.randint(0, 2)]
        }
    })


#http://www.lamda.nju.edu.cn/files/miml-image-data.rar


def ner_etl(project: Project) -> str:
    """
    Creates a jsonl file that is used for input into a vertex ai training job

    This code barely validates the requirements as listed in the vertex documentation.
    Read more about the restrictions here:
        - https://cloud.google.com/vertex-ai/docs/datasets/prepare-text#entity-extraction

    """

    #TODO: Validate the ontology:
    #  "You must supply at least 1, and no more than 100, unique labels to annotate entities that you want to extract."

    with ThreadPoolExecutor(max_workers=8) as exc:
        training_data_futures = [
            exc.submit(process_label, label)
            for label in project.label_generator()
        ]
        training_data = [future.result() for future in training_data_futures]
        training_data = [data for data in training_data if data is not None]

    # The requirement seems to only apply to training data.
    # This should be changed to check by split
    if len(training_data) < VERTEX_MIN_TRAINING_EXAMPLES:
        raise Exception("Not enought training examples provided")

    # jsonl
    training_data = training_data[:VERTEX_MAX_TRAINING_EXAMPLES]
    return "\n".join(training_data)


def main(project_id: str, gcs_bucket: str, gcs_key: str):
    gcs_client = storage.Client(project=os.environ['GOOGLE_PROJECT'])
    lb_client = Client(api_key=_labelbox_api_key)
    bucket = gcs_client.bucket(gcs_bucket)
    nowgmt = time.strftime("%Y-%m-%d_%H:%M:%S", time.gmtime())
    gcs_key = gcs_key or f'etl/ner/{nowgmt}.jsonl'
    blob = bucket.blob(gcs_key)
    project = lb_client.get_project(project_id)
    json_data = ner_etl(project)
    blob.upload_from_string(json_data)
    logger.info("ETL Complete. URI: %s", f"gs://{bucket.name}/{blob.name}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vertex AI ETL Runner')
    parser.add_argument('--gcs_bucket', type=str, required=True)
    parser.add_argument('--project_id', type=str, required=True)
    parser.add_argument('--gcs_key', type=str, required=False, default=None)
    args = parser.parse_args()
    main(**vars(args))
