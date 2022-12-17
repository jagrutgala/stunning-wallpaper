import random
from abc import ABC, abstractmethod
from typing import Tuple, List, Optional

from PIL import Image, ImageDraw


class Shape(ABC):
    @property
    @abstractmethod
    def get_bounding_box(self) -> Tuple[int, int, int, int]:
        pass

    @abstractmethod
    def isInsideShape(self, point: Tuple[int, int]) -> bool:
        pass

    @abstractmethod
    def draw_on_image(self, image: Image.Image, color_list: Tuple[int, int, int], to_fill: Optional[bool] = False) -> Image.Image:
        pass


class Circle(Shape):
    MIN_ARC_ANGLE = 0
    MAX_ARC_ANGLE = 360

    def __init__(self, center: Tuple[int, int], radius: int):
        self.center = center
        self.radius = radius

    @staticmethod
    def get_random_center(width: int, height: int, seed: Optional[int] = None) -> Tuple[int, int]:
        if seed is not None:
            random.seed(seed)
        return (random.randint(0, width), random.randint(0, height))

    @staticmethod
    def get_random_radius(max_radius: int, seed: Optional[int] = None) -> int:
        if seed is not None:
            random.seed(seed)
        return random.randint(3, max_radius)

    @property
    def get_bounding_box(self) -> Tuple[int, int, int, int]:
        return (
            self.center[0] - self.radius,  # x1
            self.center[1] - self.radius,  # y1
            self.center[0] + self.radius,  # x2
            self.center[1] + self.radius  # y2
        )

    def isInsideShape(self, point: Tuple[int, int]) -> bool:
        dist: int = (point[0] - self.center[0]) * (point[0] - self.center[0]) + \
            (point[1] - self.center[1]) * (point[1] - self.center[1])
        return dist <= (self.radius * self.radius)

    def draw_on_image(self, image: Image.Image, color: Tuple[int, int, int], to_fill: Optional[bool] = False) -> Image.Image:
        img_draw = ImageDraw.Draw(image)
        if to_fill:
            img_draw.ellipse(
                self.get_bounding_box,
                fill=color
            )
        else:
            img_draw.ellipse(
                self.get_bounding_box,
                outline=color
            )
        return image


class Rectangle(Shape):
    def __init__(self, center: Tuple[int, int], length: int, breadth: int):
        self.center = center
        self.length = length
        self.breadth = breadth

    @staticmethod
    def get_random_center(width: int, height: int, seed: Optional[int] = None) -> Tuple[int, int]:
        if seed is not None:
            random.seed(seed)
        return (random.randint(0, width), random.randint(0, height))

    @staticmethod
    def get_random_side(max_side_length: int, seed: Optional[int] = None) -> int:
        if seed is not None:
            random.seed(seed)
        return random.randint(3, max_side_length)

    @property
    def get_bounding_box(self) -> Tuple[int, int, int, int]:
        return (
            self.center[0] - (self.length//2),
            self.center[1] - (self.breadth//2),
            self.center[0] + (self.length//2),
            self.center[1] + (self.breadth//2)
        )

    def isInsideShape(self, point: Tuple[int, int]) -> bool:
        (x1, y1, x2, y2) = self.get_bounding_box
        return (
            x1 < point[0] < x2 and y1 < point[1] < y2
        )

    def draw_on_image(self, image: Image.Image, color: Tuple[int, int, int], to_fill: Optional[bool] = False) -> Image.Image:
        img_draw = ImageDraw.Draw(image)
        if to_fill:
            img_draw.rectangle(
                self.get_bounding_box,
                fill=color
            )
        else:
            img_draw.rectangle(
                self.get_bounding_box,
                outline=color
            )
        return image

# class Triangle(Shape):
#     pass
# class Hexagon(Shape):
#     pass
# class Heart(Shape):
#     pass

# def get_N_points_on_circumferrence(self, point_count: int) -> Iterable[Tuple[int, int]]:
#     cut_angle: int = 360//point_count
#     theta_list: List[int] = [i*cut_angle for i in range(point_count)]
#     for t in theta_list:
#         yield (
#             int(self.radius * math.cos(t) + self.center[0]),
#             int(self.radius * math.sin(t) + self.center[1])
#         )

# def get_N_points_on_circumferrence_rand(self, point_count: int) -> Iterable[Tuple[int, int]]:
#     for _ in range(point_count):
#         t = random.randint(0, 360)
#         yield (
#             int(self.radius * math.cos(t) + self.center[0]),
#             int(self.radius * math.sin(t) + self.center[1])
#         )

def main():
    pass


if __name__ == "__main__":
    # Code Here
    main()
