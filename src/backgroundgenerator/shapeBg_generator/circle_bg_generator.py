import sys, math, random

from typing import Iterable, Optional, Tuple, List
from PIL import Image, ImageDraw

class Circle:
    MIN_ARC_ANGLE = 0
    MAX_ARC_ANGLE = 360

    def __init__(self, center: Tuple[int ,int], radius: int):
        self.center = center
        self.radius = radius

    @staticmethod
    def get_random_center(width: int, height: int, seed: Optional[int] = None) -> Tuple[int , int]:
        if seed is not None:
            random.seed(seed)
        return (random.randint(0, width),random.randint(0, height))

    @staticmethod
    def get_random_radius(max_radius: int, seed: Optional[int] = None) -> int:
        if seed is not None:
            random.seed(seed)
        return random.randint(3, max_radius)

    @property
    def get_circle_bounding_box(self) -> Tuple[int, int, int ,int]:
        return (
            self.center[0] - self.radius, # x1
            self.center[1]- self.radius, # y1
            self.center[0] + self.radius, # x2
            self.center[1] + self.radius # y2
        )

    def isInsideCircle(self, point: Tuple[int, int]):
        dist: int = (point[0] - self.center[0]) * (point[0] - self.center[0]) + (point[1] - self.center[1]) * (point[1] - self.center[1])
        return dist <= (self.radius * self.radius)

    def get_N_points_on_circumferrence(self, point_count: int) -> Iterable[Tuple[int, int]]:
        cut_angle: int = 360//point_count
        theta_list: List[int] = [i*cut_angle for i in range(point_count)]
        for t in theta_list:
            yield (
                int(self.radius * math.cos(t) + self.center[0]),
                int(self.radius * math.sin(t) + self.center[1])
            )

    def get_N_points_on_circumferrence_rand(self, point_count: int) -> Iterable[Tuple[int, int]]:
        for _ in range(point_count):
            t = random.randint(0, 360)
            yield (
                int(self.radius * math.cos(t) + self.center[0]),
                int(self.radius * math.sin(t) + self.center[1])
            )

    def draw_on_image(self, image: Image.Image, color: Tuple[int, int, int], fill: bool = False) -> Image.Image:
        img_draw = ImageDraw.Draw(image)
        if fill:
            img_draw.ellipse(
                self.get_circle_bounding_box,
                color
            )
        else:
            img_draw.arc(
                self.get_circle_bounding_box, self.MIN_ARC_ANGLE, self.MAX_ARC_ANGLE, color
            )
        return image

def get_N_circles_rand(circle_count: int, width: int, height: int, max_radius) -> List[Circle]:
    circle_list: List[Circle] = [
        Circle(
            Circle.get_random_center(width, height),
            Circle.get_random_radius(max_radius)
        ) for _ in range(circle_count)
    ]
    return circle_list

def random_circles(width: int, height: int, color_list: List[Tuple[int, int, int]], circle_count: int, max_circle_radius: int = 50, seed: Optional[int] = None) -> Tuple[Image.Image, int]:
    image_circle = Image.new("RGB", (width, height))
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    circle_list: List[Circle] = get_N_circles_rand(circle_count, width, height, max_circle_radius)

    for circle in circle_list:
        circle.draw_on_image(image_circle, random.choice(color_list))

    return (image_circle, seed)


def nonCenter_circles(width: int, height: int, color_list: List[Tuple[int, int, int]], circle_count: int, max_circle_radius: int = 50, seed: Optional[int] = None) -> Tuple[Image.Image, int]:
    image_circle = Image.new("RGB", (width, height))
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    middle_circle: Circle = Circle((width//2, height//2), (width//3))
    circle_list: List[Circle] = get_N_circles_rand(circle_count, width, height, max_circle_radius)

    for circle in circle_list:
        if not middle_circle.isInsideCircle(circle.center):
            circle.draw_on_image(image_circle, random.choice(color_list))

    return (image_circle, seed)

def onlyCenter_circles(width: int, height: int, color_list: List[Tuple[int, int, int]], circle_count: int, max_circle_radius: int = 50, seed: Optional[int] = None) -> Tuple[Image.Image, int]:
    image_circle = Image.new("RGB", (width, height))
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    middle_circle: Circle = Circle((width//2, height//2), (width//3))
    circle_list: List[Circle] = get_N_circles_rand(circle_count, width, height, max_circle_radius)

    for circle in circle_list:
        if middle_circle.isInsideCircle(circle.center):
            circle.draw_on_image(image_circle, random.choice(color_list))

    return (image_circle, seed)

def onCircumference_circles(width: int, height: int, color_list: List[Tuple[int, int, int]], circle_count: int, max_circle_radius: int = 50, seed: Optional[int] = None) -> Tuple[Image.Image, int]:
    image_circle = Image.new("RGB", (width, height))
    if seed is None:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    middle_circle: Circle = Circle((width//2, height//2), (width//3))
    circle_center_list: List[Tuple[int, int]] = list(middle_circle.get_N_points_on_circumferrence(circle_count))

    for center in circle_center_list:
        circle: Circle = Circle(center, Circle.get_random_radius(max_circle_radius))
        circle.draw_on_image(image_circle, random.choice(color_list))

    return (image_circle, seed)

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
    alog_name: str = "onCircumference_circles"
    image, seed = onCircumference_circles(width, height, color_list, 1000, 50, seed=1)
    print(seed)
    image.save(f"./data/img_{alog_name}_{seed}.png")
    image.show()


if __name__ == "__main__":
    # Code Here
    main()
