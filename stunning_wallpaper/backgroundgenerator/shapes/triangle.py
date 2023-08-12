from math import radians
import random
import sys
from typing import List, Optional, Tuple
from typing_extensions import Self

from PIL import Image, ImageDraw
from backgroundgenerator.shapes.shape import (
    Shape,
    PointType,
    BoundingBoxType,
    RGBColorType,
)
from backgroundgenerator.shapes.point import Point


class Triangle(Shape):
    def __init__(
        self,
        vertex_1: Tuple[int, int],
        vertex_2: Tuple[int, int],
        vertex_3: Tuple[int, int],
    ):
        self.vertices: Tuple[Point, Point, Point] = (
            Point(*vertex_1),
            Point(*vertex_2),
            Point(*vertex_3),
        )
        self.center = Point(
            sum(v.x for v in self.vertices) // 3,
            sum(v.y for v in self.vertices) // 3,
        )
        super().__init__(self.center.to_tuple())

    @staticmethod
    def get_random_center(
        width: int, height: int, seed: Optional[int] = None
    ) -> Tuple[int, int]:
        if seed is not None:
            random.seed(seed)
        return (random.randint(0, width), random.randint(0, height))

    @staticmethod
    def get_random_vertex(max_side_length: int, seed: Optional[int] = None) -> int:
        if seed is not None:
            random.seed(seed)
        return random.randint(3, max_side_length)

    def get_bounding_box(self) -> BoundingBoxType:
        min_x = min([v.x for v in self.vertices])
        min_y = min([v.y for v in self.vertices])
        max_x = max([v.x for v in self.vertices])
        max_y = max([v.y for v in self.vertices])

        return (min_x, min_y, max_x, max_y)

    def is_inside_shape(self, point: PointType) -> bool:
        sides_lengths = [
            Point.calculate_distance_between(
                self.vertices[0].to_tuple(), self.vertices[1].to_tuple()
            ),
            Point.calculate_distance_between(
                self.vertices[1].to_tuple(), self.vertices[2].to_tuple()
            ),
            Point.calculate_distance_between(
                self.vertices[0].to_tuple(), self.vertices[2].to_tuple()
            ),
        ]

        for v in self.vertices:
            if Point.calculate_distance_between(v.to_tuple(), point) > max(
                sides_lengths
            ):
                return False
        return True

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
        return image

    # @classmethod
    # def get_N_triangle_rand(cls, triangle_count: int, width: int, height: int, max_side, seed: Optional[int] = None) -> Tuple[List[Self], int]:
    #     if seed is None:
    #         seed = random.randrange(sys.maxsize)
    #     random.seed(seed)
    #     triangle_list: List[Triangle] = [
    #         cls(
    #             cls.get_random_center(width, height),
    #             cls.get_random_side(max_side),
    #             cls.get_random_side(max_side)
    #         )
    #         for _ in range(triangle_count)
    #     ]
    #     return (triangle_list, seed)
