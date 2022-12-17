import math
from typing import Tuple


class RGBColor:
    """
    Represents RGB Color.
    """
    Values = ["red", "green", "blue"]
    MAX_COORD_VALUE = 1

    def __init__(self, red, green, blue):
        """
        red: float range 0-1
        green: float range 0-1
        blue: float range 0-1
        """
        self.red: float = self.__clamp_coord(red)
        self.green: float = self.__clamp_coord(green)
        self.blue: float = self.__clamp_coord(blue)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.red} {self.green} {self.blue})"

    def __str__(self, ):
        return f"({self.red}, {self.green}, {self.blue})"

    @classmethod
    def __clamp_coord(cls, coord: int) -> float:
        return min(max(coord, 0), cls.MAX_COORD_VALUE)

    @classmethod
    def __upscale_coord(cls, coord) -> int:
        """
        """
        return math.floor(coord * 255)

    @classmethod
    def from_hex(cls, hex_string: str):
        colorstring = hex_string.strip()
        if colorstring[0] == "#":
            colorstring = colorstring[1:]
        if len(colorstring) != 6:
            raise ValueError(
                "input #%s is not in #RRGGBB format" % colorstring)
        r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
        r, g, b = [int(n, 16) / 255.0 for n in (r, g, b)]
        return cls(r, g, b)


class HSVColor:
    """
    Represents HSV Color also known as HSB Color.
    """
    Values = ["hue", "saturation", "value"]
    MAX_HUE_VALUE = 360
    MAX_SATURATION_VALUE = 100
    MAX_VALUE_VALUE = 100

    def __init__(self, hue: int, saturation: int, value: int):
        """
        hue: int range 0-360
        saturation: int range 0-100
        value: int range 0-100
        """
        self.hue: int = self.__clamp_hue(hue)
        self.saturation: int = self.__clamp_saturation(saturation)
        self.value: int = self.__clamp_value(value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.hue} {self.saturation} {self.value})"

    def __str__(self, ):
        return f"({self.hue}, {self.saturation}, {self.value})"

    @classmethod
    def __clamp_hue(cls, coord):
        return min(max(coord, 0), cls.MAX_HUE_VALUE)

    @classmethod
    def __clamp_saturation(cls, coord):
        return min(max(coord, 0), cls.MAX_SATURATION_VALUE)

    @classmethod
    def __clamp_value(cls, coord):
        return min(max(coord, 0), cls.MAX_VALUE_VALUE)


class HSLColor:
    """
    Represents HSL Color.
    """
    Values = ["hue", "saturation", "lightness"]
    MAX_HUE_VALUE = 360
    MAX_SATURATION_VALUE = 100
    MAX_LIGHTNESS_VALUE = 100

    def __init__(self, hue: int, saturation: int, lightness: int):
        """
        hue: int range 0-360
        saturation: int range 0-100
        lightness: int range 0-100
        """
        self.hue: int = self.__clamp_hue(hue)
        self.saturation: int = self.__clamp_saturation(saturation)
        self.lightness: int = self.__clamp_value(lightness)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.hue} {self.saturation} {self.lightness})"

    def __str__(self, ):
        return f"({self.hue}, {self.saturation}, {self.lightness})"

    @classmethod
    def __clamp_hue(cls, coord):
        return min(max(coord, 0), cls.MAX_HUE_VALUE)

    @classmethod
    def __clamp_saturation(cls, coord):
        return min(max(coord, 0), cls.MAX_SATURATION_VALUE)

    @classmethod
    def __clamp_value(cls, coord):
        return min(max(coord, 0), cls.MAX_LIGHTNESS_VALUE)
