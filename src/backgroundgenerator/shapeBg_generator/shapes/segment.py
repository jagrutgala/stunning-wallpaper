import random
import sys
from typing import List, Optional
from typing_extensions import Self

from PIL import Image, ImageDraw

from backgroundgenerator.shapeBg_generator.shapes.shape import (
    BoundingBoxType,
    PointType,
    RGBColorType,
    Shape,
)
from backgroundgenerator.shapeBg_generator.shapes.point import Point


class Segment(Shape):
    def __init__(self, point1: PointType, point2: PointType):
        self.point1: Point = Point(*point1)
        self.point2: Point = Point(*point2)
        self.mid_point = (
            (self.point1.x + self.point2.y // 2),
            (self.point1.y + self.point2.y // 2),
        )
        super().__init__(self.mid_point)

    def __eq__(self, other: Self):
        return ((self.point1 == other.point1) and (self.point2 == other.point2)) or (
            (self.point1 == other.point2) and (self.point2 == other.point1)
        )

    def get_points(self) -> List[PointType]:
        return [self.point1.to_tuple(), self.point2.to_tuple()]

    def get_bounding_box(self) -> BoundingBoxType:
        min_x = min(self.point1.x, self.point2.x)
        max_x = min(self.point1.x, self.point2.x)
        min_y = min(self.point1.y, self.point2.y)
        max_y = min(self.point1.y, self.point2.y)

        return (min_x, min_y, max_x, max_y)

    def is_inside_shape(self, point: PointType) -> bool:
        segment_dist: float = Point.calculate_distance_between(
            self.point1.to_tuple(), self.point2.to_tuple()
        )
        to_point_dist: float = Point.calculate_distance_between(
            self.point1.to_tuple(), point
        )
        from_point_dist: float = Point.calculate_distance_between(
            self.point2.to_tuple(), point
        )

        return (from_point_dist + to_point_dist) == segment_dist

    def draw_on_image(
        self,
        image: Image.Image,
        color: RGBColorType,
        width: int = 2,
        to_fill: Optional[bool] = False,
    ) -> Image.Image:
        img_draw = ImageDraw.Draw(image)
        if to_fill:
            img_draw.line(self.get_points(), fill=color, width=width)
        else:
            img_draw.line(self.get_points(), width=width)
        return image

    @classmethod
    def get_n_segments_rand(
        cls,
        seg_count: int,
        width: int,
        height: int,
        max_dist: int,
        seed: Optional[int] = None,
    ):
        if seed is None:
            seed = random.randrange(sys.maxsize)
        random.seed(seed)
        seg_list: List[Self] = []
        for _ in range(seg_count):
            p1 = Point.get_rand_point(width, height)[0]
            p2 = Point.get_rand_point(max_dist, max_dist)[0]
            p2.x += p1.x
            p2.y += p1.y
            s = cls(p1.to_tuple(),p2.to_tuple())
            seg_list.append(s)

        return (seg_list, seed)
