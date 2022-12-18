from typing import List, Optional, Tuple

from PIL import Image

class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


    def __str__(self):
        return f"({self.x},{self.y})"


