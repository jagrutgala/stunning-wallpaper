from abc import ABC
from typing import List, Tuple
from PIL import Image


class GradientGenrationStrategy(ABC):
    def gen_func(self):
        pass


class GradientGenerator:
    def __init__(self, ggs: GradientGenrationStrategy, color_list: List[Tuple[int, int, int]]):
        self.ggs = ggs
        self.color_list = color_list

    def generate(self):
        self.ggs.gen_func()


def main():
    width = 1920
    height = 1080
    image_gardient = Image.new("RGB", (width, height))
    color_list = [
        (255, 0, 0),
        (255, 255, 0),
        (255, 255, 255),
        (255, 0, 255),
        (0, 255, 255)
    ]
    from gradientgenerator.simple_gardients import horizontal_graident, vertical_gradient
    horizontal_graident(image_gardient, color_list).show()
    vertical_gradient(image_gardient, color_list).show()


if __name__ == "__main__":
    # Code Here
    main()
