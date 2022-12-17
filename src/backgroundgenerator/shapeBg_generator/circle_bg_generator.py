import sys
import random

from typing import  Callable, Optional, Tuple, List
from PIL import Image
from common.shape import Shape, Circle

def get_N_circles_rand(circle_count: int, width: int, height: int, max_radius) -> List[Circle]:
    circle_list: List[Circle] = [
        Circle(Circle.get_random_center(width, height), Circle.get_random_radius((max_radius)))
            for _ in range(circle_count)
    ]
    return circle_list

def random_circles(width: int, height: int, color_list: List[Tuple[int, int, int]], circle_count: int, max_circle_radius: int = 50, seed: Optional[int] = None) -> Tuple[Image.Image, int]:
    image_circle = Image.new("RGB", (width, height))
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    circle_list: List[Circle] = get_N_circles_rand(
        circle_count, width, height, max_circle_radius)

    for circle in circle_list:
        circle.draw_on_image(image_circle, random.choice(color_list))

    return (image_circle, seed)


def nonCenter_circles(width: int, height: int, color_list: List[Tuple[int, int, int]], circle_count: int, max_circle_radius: int = 50, seed: Optional[int] = None) -> Tuple[Image.Image, int]:
    image_circle = Image.new("RGB", (width, height))
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    middle_circle: Circle = Circle((width//2, height//2), (width//3))
    circle_list: List[Circle] = get_N_circles_rand(
        circle_count, width, height, max_circle_radius)

    for circle in circle_list:
        if not middle_circle.isInsideShape(circle.center):
            circle.draw_on_image(image_circle, random.choice(color_list))

    return (image_circle, seed)


def onlyCenter_circles(width: int, height: int, color_list: List[Tuple[int, int, int]], circle_count: int, max_circle_radius: int = 50, seed: Optional[int] = None) -> Tuple[Image.Image, int]:
    image_circle = Image.new("RGB", (width, height))
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    middle_circle: Circle = Circle((width//2, height//2), (width//3))
    circle_list: List[Circle] = get_N_circles_rand(
        circle_count, width, height, max_circle_radius)

    for circle in circle_list:
        if middle_circle.isInsideShape(circle.center):
            circle.draw_on_image(image_circle, random.choice(color_list))

    return (image_circle, seed)


# def onCircumference_circles(width: int, height: int, color_list: List[Tuple[int, int, int]], circle_count: int, max_circle_radius: int = 50, seed: Optional[int] = None) -> Tuple[Image.Image, int]:
#     image_circle = Image.new("RGB", (width, height))
#     if seed is None:
#         seed = random.randrange(sys.maxsize)
#     random.seed(seed)

#     middle_circle: Circle = Circle((width//2, height//2), (width//3))
#     circle_center_list: List[Tuple[int, int]] = list(
#         middle_circle.get_N_points_on_circumferrence(circle_count))

#     for center in circle_center_list:
#         circle: Circle = Circle(
#             center, Circle.get_random_radius(max_circle_radius))
#         circle.draw_on_image(image_circle, random.choice(color_list))

#     return (image_circle, seed)


def main():
    width = 1920
    height = 1080
    color_list = [
        (255, 0, 0),
        (255, 255, 0),
        (255, 255, 255),
        (255, 0, 255),
        (0, 255, 255)
    ]
    alog_name: str = "random_circles"
    image, seed = random_circles(
        width, height, color_list, 500, 50, seed=20000)
    print(seed)
    image.save(f"./data/img_{alog_name}_{seed}.png")
    image.show()


if __name__ == "__main__":
    # Code Here
    main()
