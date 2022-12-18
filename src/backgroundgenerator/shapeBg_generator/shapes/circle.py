import math
import random
import sys
from typing import List, Optional, Tuple
from typing_extensions import Self

from PIL import Image, ImageDraw
from backgroundgenerator.shapeBg_generator.shapes.point import Point

from backgroundgenerator.shapeBg_generator.shapes.shape import BoundingBoxType, PointType, RGBColorType, Shape


class Circle(Shape):
    MIN_ARC_ANGLE = 0
    MAX_ARC_ANGLE = 360

    def __init__(self, center: PointType, radius: int):
        self.center: Point = Point(*center)
        self.radius = radius
        super().__init__(self.center.to_tuple())

    @staticmethod
    def get_random_center(width: int, height: int, seed: Optional[int] = None) -> PointType:
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
            self.center.y + self.radius
        )

    def get_points(self) -> List[PointType]:
        return [
            (
                int(self.radius * (math.cos(math.radians(t)))) + self.center.x,
                int(self.radius * (math.sin(math.radians(t)))) + self.center.y
            ) for t in range(0, 360, 1)
        ]

    def isInsideShape(self, point: Point) -> bool:
        dist: int = (point.x - self.center.x) * (point.x - self.center.x) + \
            (point.y - self.center.y) * (point.y - self.center.y)
        return dist <= (self.radius * self.radius)

    def draw_on_image(self, image: Image.Image, color: RGBColorType, to_fill: Optional[bool] = False) -> Image.Image:
        img_draw = ImageDraw.Draw(image)
        if to_fill:
            img_draw.polygon(
                self.get_points(),
                fill=color,
                width=2
            )
        else:
            img_draw.polygon(
                self.get_points(),
                outline=color,
                width=2
            )
        return image

    @classmethod
    def get_N_circles_rand(cls, circle_count: int, width: int, height: int, max_radius, seed: Optional[int] = None) -> Tuple[List[Self], int]:
        if seed is None:
            seed = random.randrange(sys.maxsize)
        random.seed(seed)
        circle_list: List[Self] = [
            cls(
                Point.get_rand_point(width, height)[0].to_tuple(),
                cls.get_random_radius((max_radius))
            )
            for _ in range(circle_count)
        ]

        return (circle_list, seed)
