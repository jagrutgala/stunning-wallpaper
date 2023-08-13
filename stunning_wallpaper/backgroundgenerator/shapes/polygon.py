import random
import sys
from typing import List, Optional, Tuple
from typing_extensions import Self

from PIL import Image, ImageDraw
from backgroundgenerator.shapes.point import Point

from backgroundgenerator.shapes.shape import BoundingBoxType, PointType, RGBColorType, Shape


class Polygon(Shape):
    def __init__(self, point_list: List[PointType]):
        self.point_list = [Point(*p) for p in point_list]
        self.center: Point = Point(
            topleft_corner_point.x + length // 2,
            topleft_corner_point.y + breadth//2
        )
        self.length = length
        self.breadth = breadth
        super().__init__(self.center.to_tuple())

    @staticmethod
    def get_random_center(width: int, height: int, seed: Optional[int] = None) -> PointType:
        if seed is not None:
            random.seed(seed)
        return (random.randint(0, width), random.randint(0, height))

    @staticmethod
    def get_random_side(max_side_length: int, seed: Optional[int] = None) -> int:
        if seed is not None:
            random.seed(seed)
        return random.randint(30, max_side_length)

    def get_bounding_box(self) -> BoundingBoxType:
        return (
            self.center.x - (self.length//2),
            self.center.y - (self.breadth//2),
            self.center.x + (self.length//2),
            self.center.y + (self.breadth//2)
        )

    def get_points(self) -> List[PointType]:
        return [
            (self.center.x - (self.length//2), self.center.y - (self.breadth//2)),
            (self.center.x + (self.length//2), self.center.y - (self.breadth//2)),
            (self.center.x + (self.length//2), self.center.y + (self.breadth//2)),
            (self.center.x - (self.length//2), self.center.y + (self.breadth//2))
        ]

    def is_inside_shape(self, point: Point) -> bool:
        (x1, y1, x2, y2) = self.get_bounding_box()
        return (
            x1 < point.x < x2 and y1 < point.y < y2
        )

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
    def get_n_rectangle_rand(cls, rectangle_count: int, width: int, height: int, max_side, seed: Optional[int] = None) -> Tuple[List[Self], int]:
        if seed is None:
            seed = random.randrange(sys.maxsize)
        random.seed(seed)
        rectangle_list: List[Rectangle] = [
            cls(
                Point.get_rand_point(width, height)[0].to_tuple(),
                cls.get_random_side(max_side),
                cls.get_random_side(max_side)
            )
            for _ in range(rectangle_count)
        ]
        return (rectangle_list, seed)
