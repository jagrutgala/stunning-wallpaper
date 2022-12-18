from abc import ABC, abstractmethod
import random
import sys
from typing import List, Optional, Tuple

from PIL import Image

PointType = Tuple[int, int]
BoundingBoxType = Tuple[int, int, int, int]
RGBColorType = Tuple[int, int, int]


class Shape(ABC):
    def __init__(self, position: PointType):
        self.position = position

    @abstractmethod
    def get_points(self) -> List[PointType]:
        pass

    @abstractmethod
    def get_bounding_box(self) -> BoundingBoxType:
        pass

    @abstractmethod
    def isInsideShape(self, point: PointType) -> bool:
        pass

    @abstractmethod
    def draw_on_image(self, image: Image.Image, color: RGBColorType, to_fill: Optional[bool] = False) -> Image.Image:
        pass


def get_rand_seed():
    return random.randrange(sys.maxsize)
