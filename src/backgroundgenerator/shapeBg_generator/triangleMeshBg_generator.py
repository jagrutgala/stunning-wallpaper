import random
import sys
from typing import List, Optional, Tuple
from typing_extensions import Self

from PIL import Image, ImageDraw
from scipy import spatial
from backgroundgenerator.shapeBg_generator.shapes.shape import (
    Shape,
    PointType,
    BoundingBoxType,
    RGBColorType,
)
from backgroundgenerator.shapeBg_generator.shapes.point import Point
from backgroundgenerator.shapeBg_generator.shapes.circle import Circle
from backgroundgenerator.shapeBg_generator.shapes.triangle import Triangle


def get_circumcircle(triangle: Triangle) -> Circle:
    return Circle(
        triangle.center.to_tuple(),
        int(
            Point.calculate_distance_between(
                triangle.center.to_tuple(), triangle.vertices[0].to_tuple()
            )
        ),
    )


# spatial.Delaunay()
