import random
import sys
from typing import List, Tuple

from PIL import Image, ImageFilter

from backgroundgenerator.shapeBg_generator.shapes import circle, rectangle
from backgroundgenerator.shapeBg_generator import shape_bg_generator
from backgroundgenerator.shapeBg_generator.shapes.point import Point


def main():
    width: int = 1920
    height: int = 1080

    seed = random.randrange(sys.maxsize)
    # seed = 7533460957169588469

    # (cirle_list, _seed) = circle.get_N_circles_rand(
    #     500, width, height, max_radius=50, seed=seed
    # )
    (rectangle_list, _seed) = rectangle.get_N_rectangle_rand(
        500, width, height, max_side=50, seed=seed
    )

    shape_list = []
    # shape_list.extend(cirle_list)
    shape_list.extend(rectangle_list)
    random.shuffle(shape_list)

    color_list: List[Tuple[int, int, int]] = [
        (28, 49, 94),
        (34, 124, 112),
        (136, 164, 124),
        (230, 226, 195)
    ]

    # length: int = 500
    # breadth: int = 400
    # middle_rectangle = rectangle.Rectangle(Point((width//2) - length//2, (height//2) - breadth//2), length, breadth)

    max_radius: int = 500
    middle_circle = circle.Circle(Point(width//2, height//2), 500)

    bg_image: Image.Image = Image.new("RGB", (width, height))

    # bg_image: Image.Image = shape_bg_generator.draw_shapes(bg_image, shape_list, color_list, True)
    bg_image: Image.Image = shape_bg_generator.center_shapes(bg_image, shape_list, middle_circle, color_list, True, False)

    bg_image = bg_image.filter(ImageFilter.GaussianBlur(8))
    print(seed)
    bg_image.save(
        f"./data/img_{shape_bg_generator.center_shapes.__name__}_{seed}.png")
    bg_image.show()


if __name__ == "__main__":
    # Code Here
    # for _ in range(25):
    #     main()
    main()
