import random
import sys
from typing import List, Optional, Tuple

from PIL import Image, ImageDraw

from backgroundgenerator.shapeBg_generator.shapes import shape, point
from backgroundgenerator.shapeBg_generator.shapes.point import Point


class Triangle(shape.Shape):
    def __init__(self, vertex_1: Tuple[int, int], vertex_2: Tuple[int, int], vertex_3: Tuple[int, int]):
        self.vertices: Tuple[point.Point, point.Point, point.Point] = (
            point.Point(*vertex_1),
            point.Point(*vertex_2),
            point.Point(*vertex_3)
        )
        self.center = point.Point(0, 0)
        super().__init__(self.center)

    @staticmethod
    def get_random_center(width: int, height: int, seed: Optional[int] = None) -> Tuple[int, int]:
        if seed is not None:
            random.seed(seed)
        return (random.randint(0, width), random.randint(0, height))

    @staticmethod
    def get_random_vertex(max_side_length: int, seed: Optional[int] = None) -> int:
        if seed is not None:
            random.seed(seed)
        return random.randint(3, max_side_length)

    def get_bounding_box(self) -> Tuple[int, int, int, int]:
        return (0,0,0,0)

    def isInsideShape(self, point: Point) -> bool:
        (x1, y1, x2, y2) = self.get_bounding_box()
        return (
            x1 < point.x < x2 and y1 < point.y < y2
        )

    def draw_on_image(self, image: Image.Image, color: Tuple[int, int, int], to_fill: Optional[bool] = False) -> Image.Image:
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


# def get_N_triangle_rand(triangle_count: int, width: int, height: int, max_side, seed: Optional[int] = None) -> Tuple[List[Triangle], int]:
#     if seed is None:
#         seed = random.randrange(sys.maxsize)
#     random.seed(seed)
#     triangle_list: List[Triangle] = [
#         Triangle(
#             Triangle.get_random_center(width, height),
#             Triangle.get_random_side(max_side),
#             Triangle.get_random_side(max_side)
#         )
#         for _ in range(triangle_count)
#     ]
#     return (triangle_list, seed)
