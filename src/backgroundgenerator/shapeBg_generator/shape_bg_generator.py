import random

from typing import Optional, Tuple, List, TypeVar
from PIL import Image

from backgroundgenerator.shapeBg_generator.shapes import shape

ShapeType = TypeVar("ShapeType", bound=shape.Shape)

"""
Common Option Properties
- fill
- width

"""

def draw_shapes(image: Image.Image, shape_list: List[ShapeType], color_list: List[Tuple[int, int, int]], to_fill: bool) -> Image.Image:
    for shape in shape_list:
        shape.draw_on_image(image, random.choice(color_list), to_fill)

    return image


def center_shapes(image: Image.Image, shape_list: List[ShapeType], middle_shape: ShapeType, color_list: List[Tuple[int, int, int]], to_fill: bool, center_only: bool) -> Image.Image:
    for shape in shape_list:
        is_shape_inside: bool = middle_shape.isInsideShape(shape.position)
        if not center_only:
            is_shape_inside = not is_shape_inside
        if is_shape_inside:
            shape.draw_on_image(image, random.choice(color_list), to_fill)

    return image


