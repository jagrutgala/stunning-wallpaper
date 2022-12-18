import random
import sys
from typing import List, Optional, Tuple

from PIL import Image, ImageDraw
from backgroundgenerator.shapeBg_generator.shapes.point import Point

from backgroundgenerator.shapeBg_generator.shapes.shape import Shape



class Rectangle(Shape):
    def __init__(self, topleft_corner: Point, length: int, breadth: int):
        self.center = Point(topleft_corner.x + length //
                       2, topleft_corner.y + breadth//2)
        self.length = length
        self.breadth = breadth
        super().__init__(self.center)

    @staticmethod
    def get_random_center(width: int, height: int, seed: Optional[int] = None) -> Tuple[int, int]:
        if seed is not None:
            random.seed(seed)
        return (random.randint(0, width), random.randint(0, height))

    @staticmethod
    def get_random_side(max_side_length: int, seed: Optional[int] = None) -> int:
        if seed is not None:
            random.seed(seed)
        return random.randint(10, max_side_length)

    def get_bounding_box(self) -> Tuple[int, int, int, int]:
        return (
            self.center.x - (self.length//2),
            self.center.y - (self.breadth//2),
            self.center.x + (self.length//2),
            self.center.y + (self.breadth//2)
        )

    def get_points(self) -> List[Tuple[int, int]]:
        return [
            (self.center.x - (self.length//2), self.center.y - (self.breadth//2)),
            (self.center.x + (self.length//2), self.center.y - (self.breadth//2)),
            (self.center.x + (self.length//2), self.center.y + (self.breadth//2)),
            (self.center.x - (self.length//2), self.center.y + (self.breadth//2))
        ]

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


def get_N_rectangle_rand(rectangle_count: int, width: int, height: int, max_side, seed: Optional[int] = None) -> Tuple[List[Rectangle], int]:
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)
    rectangle_list: List[Rectangle] = [
        Rectangle(
            Point(*Rectangle.get_random_center(width, height)),
            Rectangle.get_random_side(max_side),
            Rectangle.get_random_side(max_side)
        )
        for _ in range(rectangle_count)
    ]
    return (rectangle_list, seed)
