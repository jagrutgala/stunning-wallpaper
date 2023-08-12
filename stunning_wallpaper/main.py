import random
import sys
from typing import List

from PIL import Image, ImageFilter

from backgroundgenerator.background_generators import (
    gradient_mask_bg,
    rand_circle_bg,
    rand_rectangle_bg,
)
from colorgenerator.color import HSVColor, RGBColor
from colorgenerator.color_converter import ColorConverter
from colorgenerator.color_generator import (
    AnalogousColorStrategy,
    ColorStrategy,
    StaticColorStrategy,
)


def main():
    width: int = 1920
    height: int = 1080

    seed = random.randrange(sys.maxsize)
    # seed = 7967153771860395761

    bg_image: Image.Image = Image.new("RGBA", (width, height))

    cc = ColorConverter()
    color_strategy: ColorStrategy = AnalogousColorStrategy(
        cc.convert(RGBColor(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)), HSVColor),
        10,
        hue_shift=50,
        sat_shift=30,
        val_shift=60,
        seed=seed,
    )

    bg_image, _ = rand_circle_bg(
        bg_image,
        500,
        color_strategy,
        seed,
    )

    print(seed)

    bg_image.save(f"./data/img_rand_circle_bg/{seed}.png")
    # bg_image.show()


if __name__ == "__main__":
    # Code Here
    # for _ in range(25):
    #     main()
    for _ in range(10):
        main()


# bg_image, _ = gradient_mask_bg(
#     bg_image,
#     color_strategy,
#     rand_circle_bg(bg_image, 500, StaticColorStrategy([HSVColor(0, 0, 100)]), seed)[
#         0
#     ],
#     seed,
# )
