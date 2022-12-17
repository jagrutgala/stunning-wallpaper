import sys
import random

from typing import  Callable, Optional, Tuple, List
from PIL import Image
from common.shape import Rectangle

def get_N_rectangle_rand(rectangle_count: int, width: int, height: int, max_side) -> List[Rectangle]:
    rectangle_list: List[Rectangle] = [
        Rectangle(
            Rectangle.get_random_center(width, height),
            Rectangle.get_random_side(max_side),
            Rectangle.get_random_side(max_side)
        )
            for _ in range(rectangle_count)
    ]
    return rectangle_list

def random_rectangles(width: int, height: int, color_list: List[Tuple[int, int, int]], rectangle_count: int, max_rectangle_side: int, seed: Optional[int] = None) -> Tuple[Image.Image, int]:
    image_rectangle = Image.new("RGB", (width, height))
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    rectangle_list: List[Rectangle] = get_N_rectangle_rand(
        rectangle_count, width, height, max_rectangle_side)

    for rectangle in rectangle_list:
        rectangle.draw_on_image(image_rectangle, random.choice(color_list))

    return (image_rectangle, seed)


def nonCenter_rectangles(width: int, height: int, color_list: List[Tuple[int, int, int]], rectangle_count: int, max_rectangle_side: int, seed: Optional[int] = None) -> Tuple[Image.Image, int]:
    image_rectangle = Image.new("RGB", (width, height))
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    middle_rectangle: Rectangle = Rectangle((width//2, height//2), (width//3), (width//4))
    rectangle_list: List[Rectangle] = get_N_rectangle_rand(
        rectangle_count, width, height, max_rectangle_side)

    for rectangle in rectangle_list:
        if not middle_rectangle.isInsideShape(rectangle.center):
            rectangle.draw_on_image(image_rectangle, random.choice(color_list))

    return (image_rectangle, seed)


def onlyCenter_rectangles(width: int, height: int, color_list: List[Tuple[int, int, int]], rectangle_count: int, max_rectangle_side: int, seed: Optional[int] = None) -> Tuple[Image.Image, int]:
    image_rectangle = Image.new("RGB", (width, height))
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    middle_rectangle: Rectangle = Rectangle((width//2, height//2), (width//3), (width//4))
    rectangle_list: List[Rectangle] = get_N_rectangle_rand(
        rectangle_count, width, height, max_rectangle_side)

    for rectangle in rectangle_list:
        if middle_rectangle.isInsideShape(rectangle.center):
            rectangle.draw_on_image(image_rectangle, random.choice(color_list))

    return (image_rectangle, seed)


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
    alog_name: str = nonCenter_rectangles.__name__
    image, seed = nonCenter_rectangles(
        width, height, color_list, 500, 100, seed=20000)
    print(seed)
    image.save(f"./data/img_{alog_name}_{seed}.png")
    image.show()


if __name__ == "__main__":
    # Code Here
    main()
