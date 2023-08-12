import random
import sys
from typing import List, Optional, Tuple, Type
import numpy as np
from PIL import Image, ImageDraw
from backgroundgenerator.shapes.point import Point
from backgroundgenerator.shapes.circle import Circle
from backgroundgenerator.shapes.rectangle import Rectangle
from backgroundgenerator.shapes.shape import Shape
from colorgenerator.color import HSVColor, RGBColor
from colorgenerator.color_converter import ColorConverter
from colorgenerator.color_generator import AnalogousColorStrategy, ColorStrategy, StaticColorStrategy


cc = ColorConverter()


def rand_circle_bg(
    image: Image.Image,
    no_of_shapes: int,
    color_strategy: ColorStrategy,
    seed: Optional[int] = None,
) -> Tuple[Image.Image, int]:
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    circles, _ = Circle.get_n_circles_rand(
        no_of_shapes, image.size[0], image.size[1], 60, seed
    )

    color_list: List[HSVColor] = color_strategy.getColors()

    for shape in circles:
        rgb: RGBColor = cc.convert(random.choice(color_list), RGBColor)
        shape.draw_on_image(image, rgb.to_tuple(), to_fill=True)

    return (image, seed)


def rand_rectangle_bg(
    image: Image.Image,
    no_of_shapes: int,
    color_strategy: ColorStrategy,
    seed: Optional[int] = None,
) -> Tuple[Image.Image, int]:
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    rectangles, _ = Rectangle.get_n_rectangle_rand(
        no_of_shapes, image.size[0], image.size[1], 150, seed
    )

    color_list: List[HSVColor] = color_strategy.getColors()

    for shape in rectangles:
        rgb: RGBColor = cc.convert(random.choice(color_list), RGBColor)
        shape.draw_on_image(image, rgb.to_tuple(), to_fill=True)

    return (image, seed)


def gradient_mask_bg(
    image: Image.Image,
    color_strategy: ColorStrategy,
    mask_image: Image.Image,
    seed: Optional[int] = None,
) -> Tuple[Image.Image, int]:
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    color_list = [cc.convert(c, RGBColor) for c in color_strategy.getColors()]

    if len(color_list) < 4:
        raise ValueError("Insuficient number of colors in strategy (must be >= 4)")

    c1, c2, c3, c4 = random.sample(color_list, k=4)
    r = np.linspace(
        np.linspace(c1.red, c4.red, image.height),
        np.linspace(c2.red, c3.red, image.height),
        image.width,
    )
    g = np.linspace(
        np.linspace(c1.green, c4.green, image.height),
        np.linspace(c2.green, c3.green, image.height),
        image.width,
    )
    b = np.linspace(
        np.linspace(c1.blue, c4.blue, image.height),
        np.linspace(c2.blue, c3.blue, image.height),
        image.width,
    )
    im_arr = np.array([r, g, b]).T
    image = Image.fromarray(np.uint8(im_arr * 255)).convert("RGBA")

    result_image = Image.composite(image, mask_image, mask_image.convert("L"))

    return (result_image, seed)


def zig_zag_pathches(
    image: Image.Image,
    color_strategy: ColorStrategy,
    zz_count: int,
    horizon_intercept: int,
    zz_var: int,
    zz_height: int,
    seed: Optional[int] = None,
) -> Tuple[Image.Image, int]:
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    color_list = color_strategy.getColors()
    zig_zag_points = [
        Point(i, horizon_intercept + random.randint(-zz_var // 2, zz_var // 2))
        for i in range(0, image.width + 25, 25)
    ]

    zig_zag_points.extend(
        reversed([Point(p.x, p.y + zz_height) for p in zig_zag_points])
    )
    for z in range(0, zz_count):
        new_zig_zag_points = [Point(p.x, p.y + (z * 20)) for p in zig_zag_points]

        cc.convert(random.choice(color_list), RGBColor)
        img_draw = ImageDraw.Draw(image)
        img_draw.polygon(
            [p.to_tuple() for p in new_zig_zag_points],
            fill=cc.convert(random.choice(color_list), RGBColor).to_tuple(),
            width=2,
        )

    return image, seed


def rand_intersecting_circle_bg(
    image: Image.Image,
    base_circle: Circle,
    no_of_shapes: int,
    color_strategy: ColorStrategy,
    seed: Optional[int] = None,
) -> Tuple[Image.Image, int]:
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    circles, _ = Circle.get_n_circles_rand(
        no_of_shapes, image.size[0], image.size[1], 60, seed
    )
    circles = list(filter(lambda c: c.radius>10, circles))
    circles = sorted(circles, key=lambda c: c.radius, reverse=True)
    intersecting_circles: List[Circle] = [base_circle]
    for c1 in circles:
        icList = circles.copy()
        for c2 in icList:
            if c1 == c2 or c2 in intersecting_circles:
                continue
            check_dist = abs(c1.center.x - c2.center.x)
            if not (check_dist < max(c1.radius, c2.radius)):
                continue
            if Point.calculate_distance_between(c1.center.to_tuple(), c2.center.to_tuple()) < (c1.radius + c2.radius):
                print(f"circle passed {c1} intersecting with {c2}")
                intersecting_circles.extend([c1, c2])
                break

    color_list: List[HSVColor] = color_strategy.getColors()
    intersecting_circles = sorted(intersecting_circles, key=lambda c: c.radius, reverse=True)
    print(f"drawing {len(intersecting_circles)} circles")
    for shape in intersecting_circles:
        rgb: RGBColor = cc.convert(random.choice(color_list), RGBColor)
        shape.draw_on_image(image, rgb.to_tuple(), to_fill=True)

    return (image, seed)


def center_piece_and_line_bg(
    image: Image.Image,
    base_shape: Shape,
    line_list: List[Shape],
    color_strategy: ColorStrategy
):
    ...

if __name__ == "__main__":
    # Code Here

    # zig zag
    tmpimage, _s = zig_zag_pathches(
        Image.new("RGB", (1920, 1080)),
        AnalogousColorStrategy(cc.convert(RGBColor(23, 73, 162), HSVColor), 20),
        30,
        100,
        20,
        800,
        7967153771860395761,
    )

    # rand circle
    # tmpimage, _s = rand_circle_bg(
    #     Image.new("RGB", (1920, 1080)),
    #     100,
    #     StaticColorStrategy([cc.convert(RGBColor(23, 73, 162), HSVColor)]),
    #     # 7967153771860395761,
    # )
    # Circle((1920//2, 1080//2), 100).draw_on_image(tmpimage, RGBColor(23, 73, 162).to_tuple(), to_fill=True)

    # intersecting circle
    # tmpimage, _s = rand_intersecting_circle_bg(
    #     Image.new("RGB", (1920, 1080)),
    #     Circle((1920//2, 1080//2), 300),
    #     250,
    #     AnalogousColorStrategy(cc.convert(RGBColor(23, 73, 162), HSVColor), 20),
    #     # 7967153771860395761,
    # )

    print(_s)
    tmpimage.show()
