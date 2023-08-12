import random

from typing import Optional, Tuple, List, Type, TypeVar
from PIL import Image

from backgroundgenerator.shapes.shape import Shape, PointType, BoundingBoxType, RGBColorType
from backgroundgenerator.shapes.segment import Segment
# from backgroundgenerator.shapes.triangle import Triangle
from backgroundgenerator.shapes.rectangle import Rectangle
from backgroundgenerator.shapes.circle import Circle

ShapeType = TypeVar("ShapeType", bound=Shape)

"""
Common Option Properties
- fill
- width

"""


def draw_shapes_rand(image: Image.Image, shape_list: List[ShapeType], color_list: List[Tuple[int, int, int]], to_fill: bool) -> Image.Image:
    for shape in shape_list:
        shape.draw_on_image(image, random.choice(color_list), to_fill)

    return image


def draw_center_shapes_rand(image: Image.Image, shape_list: List[ShapeType], middle_shape: ShapeType, color_list: List[Tuple[int, int, int]], to_fill: bool, center_only: bool) -> Image.Image:
    for shape in shape_list:
        x1, y1, x2, y2 = shape.get_bounding_box()
        is_shape_inside: bool = middle_shape.is_inside_shape(
            (x1, y1)) and middle_shape.is_inside_shape((x2, y2))
        if not center_only:
            is_shape_inside = not is_shape_inside
        if is_shape_inside:
            shape.draw_on_image(image, random.choice(color_list), to_fill)

    return image


def draw_inverted_shape_mask(image: Image.Image, shape_list: List[ShapeType], middle_shape: ShapeType, color_list: List[Tuple[int, int, int]], to_fill: bool, center_only: bool) -> Image.Image:
    return image


def shape_mosaic(image: Image.Image, shape_type: Type[ShapeType], color_list: List[Tuple[int, int, int]], to_fill: bool) -> Image.Image:
    return image


def overlapping_shapes_mosaic(image: Image.Image, shape_type: Type[ShapeType], color_list: List[Tuple[int, int, int]], to_fill: bool) -> Image.Image:
    return image


def layered_shapes_rand(image: Image.Image, layer_width: int, color_list: List[Tuple[int, int, int]]) -> Image.Image:
    return image


# def connected_shapes_rand(image: Image.Image, shape_list: List[ShapeType], color: Tuple[int, int, int], to_fill: bool) -> Image.Image:
#     if (len(shape_list)) <= 0:
#         raise ValueError("shape_list length must be > 1")

#     shape_list[0].draw_on_image(image, color, to_fill)
#     point1: PointType = shape_list[0].position
#     for shape in shape_list[1:]:
#         shape.draw_on_image(image, color, to_fill)
#         segment: Segment = Segment(point1, shape.position)
#         segment.draw_on_image(image, color, 5, to_fill)
#         point1: PointType = shape.position
#     return image


def inside_shape_bump(image: Image.Image) -> Image.Image:
    return image
