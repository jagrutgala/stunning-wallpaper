import math
import random
from typing import List, Optional, Tuple
from typing_extensions import Self

from PIL import Image, ImageDraw

from backgroundgenerator.shapeBg_generator.shapes.shape import (
    BoundingBoxType,
    PointType,
    RGBColorType,
    Shape,
    get_rand_seed,
)


class Point(Shape):
    @classmethod
    def calculate_distance_between(cls, p1: PointType, p2: PointType) -> float:
        point1, point2 = cls(*p1), cls(*p2)
        return math.dist(point1.to_tuple(), point2.to_tuple())

    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        super().__init__(self.to_tuple())

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def __eq__(self, other: Self):
        return sorted(self.to_tuple()) == sorted(other.to_tuple())

    def to_tuple(self) -> PointType:
        return (self.x, self.y)

    def get_points(self) -> List[PointType]:
        return [self.to_tuple()]

    def get_bounding_box(self) -> BoundingBoxType:
        (x1, y1) = self.to_tuple()
        return (x1, y1, x1, y1)

    def is_inside_shape(self, point: PointType) -> bool:
        return point == self.to_tuple()

    def translate(self, vector: PointType) -> Self:
        return super().translate(vector)

    def rotate(self, angle: float) -> Self:
        return super().rotate(angle)

    def draw_on_image(
        self,
        image: Image.Image,
        color: RGBColorType,
        width: int = 2,
        to_fill: Optional[bool] = False,
    ) -> Image.Image:
        img_draw = ImageDraw.Draw(image)
        img_draw.point(self.get_points(), fill=color)

        return image

    @classmethod
    def get_rand_point(
        cls, width: int, height: int, seed: Optional[int] = None
    ) -> Tuple[Self, int]:
        if seed is None:
            seed = get_rand_seed()
        random.seed(seed)
        return (cls(random.randint(0, width), random.randint(0, height)), seed)

    @classmethod
    def get_n_point_rand(
        cls, point_count: int, width: int, height: int, seed: Optional[int] = None
    ) -> Tuple[List[Self], int]:
        if seed is None:
            seed = get_rand_seed()
        random.seed(seed)
        rectangle_list: List[Self] = [
            cls(random.randint(0, width), random.randint(0, height))
            for _ in range(point_count)
        ]

        return (rectangle_list, seed)
