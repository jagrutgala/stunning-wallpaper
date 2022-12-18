from typing import List, Optional
from backgroundgenerator.shapeBg_generator.shapes.point import Point
from backgroundgenerator.shapeBg_generator.shapes.shape import BoundingBoxType, PointType, RGBColorType, Shape

from PIL import Image, ImageDraw

class Segment(Shape):
    def __init__(self, point1: PointType, point2: PointType):
        self.point1: Point = Point(*point1)
        self.point2: Point = Point(*point2)
        self.mid_point = Point(*point1)
        super().__init__(self.mid_point.to_tuple())

    def get_points(self) -> List[PointType]:
        return [
            self.point1.to_tuple(), self.point2.to_tuple()
        ]

    def get_bounding_box(self) -> BoundingBoxType:
        pass

    def isInsideShape(self, point: PointType) -> bool:
        # point lies on line
        pass

    def draw_on_image(self, image: Image.Image, color: RGBColorType, to_fill: Optional[bool] = False) -> Image.Image:
        img_draw = ImageDraw.Draw(image)
        if to_fill:
            img_draw.line(
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
