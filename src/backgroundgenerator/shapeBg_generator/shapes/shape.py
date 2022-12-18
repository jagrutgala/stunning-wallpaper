from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from PIL import Image

from backgroundgenerator.shapeBg_generator.shapes import point


class Shape(ABC):
    def __init__(self, position: point.Point):
        self.position = position

    @abstractmethod
    def get_points(self) -> List[Tuple[int, int]]:
        pass

    @abstractmethod
    def get_bounding_box(self) -> Tuple[int, int, int, int]:
        pass

    @abstractmethod
    def isInsideShape(self, point: point.Point) -> bool:
        pass

    @abstractmethod
    def draw_on_image(self, image: Image.Image, color_list: Tuple[int, int, int], to_fill: Optional[bool] = False) -> Image.Image:
        pass
