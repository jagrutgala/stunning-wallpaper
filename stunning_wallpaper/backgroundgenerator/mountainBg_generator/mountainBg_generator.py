import random
import sys
from typing import List, Optional, Tuple, Type, TypeVar

import numpy as np
from backgroundgenerator.shapes.rectangle import Rectangle
from backgroundgenerator.shapes.segment import Segment
from PIL import Image

from colorgenerator.color import HSVColor, RGBColor
from colorgenerator.color_converter import ColorConverter
from colorgenerator.color_generator import (
    AnalogousColorStrategy,
    ColorStrategy,
)


def draw_mountain_layers_rand(
    image: Image.Image,
    color_strategy: ColorStrategy,
    to_fill: bool,
    seed: Optional[int] = None,
) -> Tuple[Image.Image, int]:
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    width, height = image.size

    noOfStrips = random.choices([4, 5, 6, 7, 8], cum_weights=(5, 20, 60, 10, 5), k=1)
    nPoints = random.choices([1, 2, 3, 4, 5], cum_weights=(5, 20, 60, 10, 5), k=noOfStrips[0])



    return image, seed


def main():
    width: int = 1920
    height: int = 1080

    seed = random.randrange(sys.maxsize)
    # seed = 7967153771860395761

    bg_image: Image.Image = Image.new("RGBA", (width, height))

    cc = ColorConverter()
    color_strategy: ColorStrategy = AnalogousColorStrategy(
        cc.convert(
            RGBColor(
                random.randint(100, 255),
                random.randint(100, 255),
                random.randint(100, 255),
            ),
            HSVColor,
        ),
        10,
        hue_shift=50,
        sat_shift=30,
        val_shift=60,
        seed=seed,
    )

    bg_image, _ = draw_mountain_layers_rand(bg_image, color_strategy, False, seed)

    print(seed)


if __name__ == "__main__":
    main()
