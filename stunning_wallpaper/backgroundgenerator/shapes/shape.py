from abc import ABC, abstractclassmethod, abstractmethod
import random
import sys
from typing import Any, Callable, List, Optional, Tuple
from typing_extensions import Self

from PIL import Image

PointType = Tuple[int, int]
BoundingBoxType = Tuple[int, int, int, int]
RGBColorType = Tuple[int, int, int]


class Shape(ABC):
    def __init__(self, position: PointType):
        self.position = position

    @abstractmethod
    def get_points(self) -> List[PointType]:
        ...

    @abstractmethod
    def get_bounding_box(self) -> BoundingBoxType:
        ...

    @abstractmethod
    def is_inside_shape(self, point: PointType) -> bool:
        ...

    @abstractmethod
    def translate(self, vector: PointType) -> Self:
        ...

    @abstractmethod
    def rotate(self, angle: float) -> Self:
        ...

    @abstractmethod
    def draw_on_image(
        self,
        image: Image.Image,
        color: RGBColorType,
        width: int = 2,
        to_fill: Optional[bool] = False,
    ) -> Image.Image:
        ...


def get_rand_seed():
    return random.randrange(sys.maxsize)
