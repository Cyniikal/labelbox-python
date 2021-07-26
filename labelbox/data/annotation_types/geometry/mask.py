from typing import Callable, Tuple, Union

import numpy as np
from pydantic.class_validators import validator
from rasterio.features import shapes
from shapely.geometry import MultiPolygon, shape

from ..data.raster import RasterData
from .geometry import Geometry


class Mask(Geometry):
    # Raster data can be shared across multiple masks... or not
    mask: RasterData
    # RGB or Grayscale
    color: Union[int, Tuple[int, int, int]]

    @property
    def geometry(self):
        mask = self.raster(binary=True)
        polygons = (
            shape(shp)
            for shp, val in shapes(mask, mask=None)
            # ignore if shape is area of smaller than 1 pixel
            if val >= 1)
        return MultiPolygon(polygons).__geo_interface__

    def raster(self, binary=False) -> np.ndarray:
        """
        Removes all pixels from the segmentation mask that do not equal self.color

        Returns:
            np.ndarray representing only this object
        """
        mask = self.mask.data
        if len(mask.shape) == 2:
            mask = np.expand_dims(mask, axis=-1)
        mask = np.alltrue(mask == self.color, axis=2).astype(np.uint8)
        if binary:
            return mask
        elif isinstance(self.color, int):
            return mask * self.color
        else:
            color_image = np.zeros((mask.shape[0], mask.shape[1], 3),
                                   dtype=np.uint8)
            color_image[mask.astype(np.bool)] = self.color
            return color_image

    def create_url(self, signer: Callable[[bytes], str]) -> str:
        """
        Update the segmentation mask to have a url.
        Only update the mask if it doesn't already have a url

        Args:
            signer: A function that accepts bytes and returns a signed url.
        Returns:
            the url for the mask
        """
        return self.mask.create_url(signer)

    @validator('color')
    def is_valid_color(cls, color):
        #Does the dtype matter? Can it be a float?
        if isinstance(color, (tuple, list)):
            if len(color) != 3:
                raise ValueError(
                    "Segmentation colors must be either a (r,g,b) tuple or a single grayscale value"
                )
            elif not all([0 <= c <= 255 for c in color]):
                raise ValueError(
                    f"All rgb colors must be between 0 and 255. Found : {color}"
                )
        elif not (0 <= color <= 255):
            raise ValueError(
                f"All rgb colors must be between 0 and 255. Found : {color}")

        return color