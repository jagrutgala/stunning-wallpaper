import random
import sys
from typing import List, Optional, Tuple
from typing_extensions import Self

from PIL import Image, ImageDraw
from scipy import spatial
from backgroundgenerator.shapes.shape import (
    Shape,
    PointType,
    BoundingBoxType,
    RGBColorType,
)
from backgroundgenerator.shapes.point import Point
from backgroundgenerator.shapes.circle import Circle
from backgroundgenerator.shapes.triangle import Triangle


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
