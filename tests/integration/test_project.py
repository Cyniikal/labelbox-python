import json

import pytest
import requests

from labelbox import Project, LabelingFrontend
from labelbox.exceptions import InvalidQueryError
from labelbox.schema.project import QueueMode


def test_project(client, rand_gen):
    before = list(client.get_projects())
    for o in before:
        assert isinstance(o, Project)

    data = {"name": rand_gen(str), "description": rand_gen(str)}
    project = client.create_project(**data)
    assert project.name == data["name"]
    assert project.description == data["description"]

    after = list(client.get_projects())
    assert len(after) == len(before) + 1
    assert project in after

    project = client.get_project(project.uid)
    assert project.name == data["name"]
    assert project.description == data["description"]

    update_data = {"name": rand_gen(str), "description": rand_gen(str)}
    project.update(**update_data)
    # Test local object updates.
    assert project.name == update_data["name"]
    assert project.description == update_data["description"]

    # Test remote updates.
    project = client.get_project(project.uid)
    assert project.name == update_data["name"]
    assert project.description == update_data["description"]

    project.delete()
    final = list(client.get_projects())
    assert project not in final
    assert set(final) == set(before)


@pytest.mark.skip(
    reason="this will fail if run multiple times, limit is defaulted to 3 per org"
    "add this back in when either all test orgs have unlimited, or we delete all tags befoer running"
)
def test_update_project_resource_tags(client, rand_gen):
    before = list(client.get_projects())
    for o in before:
        assert isinstance(o, Project)

    org = client.get_organization()
    assert org.uid is not None

    project_name = rand_gen(str)
    p1 = client.create_project(name=project_name)
    assert p1.uid is not None

    colorA = "#ffffff"
    textA = rand_gen(str)
    tag = {"text": textA, "color": colorA}

    colorB = colorA
    textB = rand_gen(str)
    tagB = {"text": textB, "color": colorB}

    tagA = client.get_organization().create_resource_tag(tag)
    assert tagA.text == textA
    assert '#' + tagA.color == colorA
    assert tagA.uid is not None

    tags = org.get_resource_tags()
    lenA = len(tags)
    assert lenA > 0

    tagB = client.get_organization().create_resource_tag(tagB)
    assert tagB.text == textB
    assert '#' + tagB.color == colorB
    assert tagB.uid is not None

    tags = client.get_organization().get_resource_tags()
    lenB = len(tags)
    assert lenB > 0
    assert lenB > lenA

    project_resource_tag = client.get_project(
        p1.uid).update_project_resource_tags([str(tagA.uid)])
    assert len(project_resource_tag) == 1
    assert project_resource_tag[0].uid == tagA.uid


def test_project_filtering(client, rand_gen):
    name_1 = rand_gen(str)
    name_2 = rand_gen(str)
    p1 = client.create_project(name=name_1)
    p2 = client.create_project(name=name_2)

    assert list(client.get_projects(where=Project.name == name_1)) == [p1]
    assert list(client.get_projects(where=Project.name == name_2)) == [p2]

    p1.delete()
    p2.delete()


def test_upsert_review_queue(project):
    project.upsert_review_queue(0.6)

    with pytest.raises(ValueError) as exc_info:
        project.upsert_review_queue(1.001)
    assert str(exc_info.value) == "Quota factor must be in the range of [0,1]"

    with pytest.raises(ValueError) as exc_info:
        project.upsert_review_queue(-0.001)
    assert str(exc_info.value) == "Quota factor must be in the range of [0,1]"


def test_extend_reservations(project):
    assert project.extend_reservations("LabelingQueue") == 0
    assert project.extend_reservations("ReviewQueue") == 0
    with pytest.raises(InvalidQueryError):
        project.extend_reservations("InvalidQueueType")


def test_attach_instructions(client, project):
    with pytest.raises(ValueError) as execinfo:
        project.upsert_instructions('tests/integration/media/sample_pdf.pdf')
    assert str(
        execinfo.value
    ) == "Cannot attach instructions to a project that has not been set up."

    editor = list(
        client.get_labeling_frontends(
            where=LabelingFrontend.name == "editor"))[0]
    empty_ontology = {"tools": [], "classifications": []}
    project.setup(editor, empty_ontology)

    project.upsert_instructions('tests/integration/media/sample_pdf.pdf')
    assert json.loads(
        list(project.labeling_frontend_options())
        [-1].customization_options).get('projectInstructions') is not None

    with pytest.raises(ValueError) as exc_info:
        project.upsert_instructions('/tmp/file.invalid_file_extension')
    assert "instructions_file must be a pdf or html file. Found" in str(
        exc_info.value)


def test_html_instructions(configured_project):
    html_file_path = '/tmp/instructions.html'
    sample_html_str = "<html></html>"

    with open(html_file_path, 'w') as file:
        file.write(sample_html_str)

    configured_project.upsert_instructions(html_file_path)
    updated_ontology = configured_project.ontology().normalized

    instructions = updated_ontology.pop('projectInstructions')
    assert requests.get(instructions).text == sample_html_str


def test_same_ontology_after_instructions(
        configured_project_with_complex_ontology):
    project, _ = configured_project_with_complex_ontology
    initial_ontology = project.ontology().normalized
    project.upsert_instructions('tests/data/assets/loremipsum.pdf')
    updated_ontology = project.ontology().normalized

    instructions = updated_ontology.pop('projectInstructions')

    assert initial_ontology == updated_ontology
    assert instructions is not None


def test_queued_data_row_export(configured_project):
    result = configured_project.export_queued_data_rows()
    assert len(result) == 1


def test_queue_mode(configured_project: Project):
    assert configured_project.queue_mode() == QueueMode.Dataset
    configured_project.update(queue_mode=QueueMode.Batch)
    assert configured_project.queue_mode() == QueueMode.Batch
