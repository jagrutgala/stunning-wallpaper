import math
import random
import sys
from typing import List, Optional, Tuple
from typing_extensions import Self

from PIL import Image, ImageDraw
from backgroundgenerator.shapes.point import Point

from backgroundgenerator.shapes.shape import (
    BoundingBoxType,
    PointType,
    RGBColorType,
    Shape,
)

class Circle(Shape):
    MIN_ARC_ANGLE = 0
    MAX_ARC_ANGLE = 360

    def __init__(self, center: PointType, radius: int):
        self.center: Point = Point(*center)
        self.radius = radius
        super().__init__(self.center.to_tuple())
        self.debug_message = f"{self.center.to_tuple()}-{self.radius}"

    def __repr__(self) -> str:
        return f"center: {self.center.to_tuple()} - radius: {self.radius}"

    def __eq__(self, __o: Self) -> bool:
        return self.center.to_tuple() == __o.center.to_tuple() and self.radius == __o.radius

    @staticmethod
    def get_random_center(
        width: int, height: int, seed: Optional[int] = None
    ) -> PointType:
        if seed is not None:
            random.seed(seed)
        return (random.randint(0, width), random.randint(0, height))

    @staticmethod
    def get_random_radius(max_radius: int, seed: Optional[int] = None) -> int:
        if seed is not None:
            random.seed(seed)
        return random.randint(3, max_radius)

    def get_bounding_box(self) -> BoundingBoxType:
        return (
            self.center.x - self.radius,
            self.center.y - self.radius,
            self.center.x + self.radius,
            self.center.y + self.radius,
        )

    def get_points(self) -> List[PointType]:
        return [
            (
                int(self.radius * (math.cos(math.radians(t)))) + self.center.x,
                int(self.radius * (math.sin(math.radians(t)))) + self.center.y,
            )
            for t in range(0, 360, 1)
        ]

    def is_inside_shape(self, point: PointType) -> bool:
        p: Point = Point(*point)
        dist: int = (p.x - self.center.x) * (p.x - self.center.x) + (
            p.y - self.center.y
        ) * (p.y - self.center.y)
        return dist <= (self.radius * self.radius)

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
        if to_fill:
            img_draw.polygon(self.get_points(), fill=color, width=width)
        else:
            img_draw.polygon(self.get_points(), outline=color, width=width)
        # text_size_point = Point(*img_draw.textsize(self.debug_message))
        # img_draw.text((self.center.x - text_size_point.x//2, self.center.y - text_size_point.y//2), self.debug_message)
        return image

    @classmethod
    def get_n_circles_rand(
        cls,
        circle_count: int,
        width: int,
        height: int,
        max_radius,
        seed: Optional[int] = None,
    ) -> Tuple[List[Self], int]:
        if seed is None:
            seed = random.randrange(sys.maxsize)
        random.seed(seed)
        circle_list: List[Self] = [
            cls(
                Point.get_rand_point(width, height)[0].to_tuple(),
                cls.get_random_radius((max_radius)),
            )
            for _ in range(circle_count)
        ]

        return (circle_list, seed)
