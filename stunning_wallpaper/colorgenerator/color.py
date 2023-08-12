import math
from typing import Union


class RGBColor:
    """
    Represents RGB Color.
    """

    Values = ["red", "green", "blue"]
    MAX_COORD_VALUE = 1
    UPSCALE_MAX_COORD_VALUE = 255

    def __init__(self, red: int, green: int, blue: int):
        """
        red: float range 0-255
        green: float range 0-255
        blue: float range 0-255
        """
        self.red: float = self._clamp_coord(red / self.UPSCALE_MAX_COORD_VALUE)
        self.green: float = self._clamp_coord(green / self.UPSCALE_MAX_COORD_VALUE)
        self.blue: float = self._clamp_coord(blue / self.UPSCALE_MAX_COORD_VALUE)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.red} {self.green} {self.blue})"

    def __str__(
        self,
    ):
        return f"({self.red}, {self.green}, {self.blue})"

    @classmethod
    def _clamp_coord(cls, coord: float) -> float:
        return min(max(coord, 0), cls.MAX_COORD_VALUE)

    @classmethod
    def _upscale_coord(cls, coord: float) -> int:
        """ """
        return math.floor(coord * 255)

    @classmethod
    def from_hex(cls, hex_string: str):
        colorstring = hex_string.strip()
        if colorstring[0] == "#":
            colorstring = colorstring[1:]
        if len(colorstring) != 6:
            raise ValueError("input #%s is not in #RRGGBB format" % colorstring)
        r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
        r, g, b = [int(n, 16) for n in (r, g, b)]
        return cls(r, g, b)

    def to_tuple(self):
        return (
            self._upscale_coord(self.red),
            self._upscale_coord(self.green),
            self._upscale_coord(self.blue),
        )


class HSVColor:
    """
    Represents HSV Color also known as HSB Color.
    """

    Values = ["hue", "saturation", "value"]
    MAX_HUE_VALUE = 360
    MAX_SATURATION_VALUE = 1
    MAX_VALUE_VALUE = 1

    def __init__(self, hue: int, saturation: float, value: float):
        """
        hue: int range 0-360
        saturation: int range 0-100
        value: int range 0-100
        """
        self.hue: int = self.clamp_hue(hue)
        self.saturation: float = self.clamp_saturation(saturation / 100.0)
        self.value: float = self.clamp_value(value / 100.0)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.hue} {self.saturation} {self.value})"

    def __str__(self):
        return f"({self.hue}, {self.saturation}, {self.value})"

    @classmethod
    def clamp_hue(cls, coord: int):
        return min(max(coord, 0), cls.MAX_HUE_VALUE)

    @classmethod
    def clamp_saturation(cls, coord: float):
        return min(max(coord, 0), cls.MAX_SATURATION_VALUE)

    @classmethod
    def clamp_value(cls, coord: float):
        return min(max(coord, 0), cls.MAX_VALUE_VALUE)

    @classmethod
    def upscale_sat_val(cls, sat_val: float):
        return sat_val * 100


class HSLColor:
    """
    Represents HSL Color.
    """

    Values = ["hue", "saturation", "lightness"]
    MAX_HUE_VALUE = 360
    MAX_SATURATION_VALUE = 1
    MAX_LIGHTNESS_VALUE = 1

    def __init__(self, hue: int, saturation: float, lightness: float):
        """
        hue: int range 0-360
        saturation: int range 0-100
        lightness: int range 0-100
        """
        self.hue: int = self.__clamp_hue(hue)
        self.saturation: int = self.__clamp_saturation(saturation / 100)
        self.lightness: int = self.__clamp_value(lightness / 100)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.hue} {self.saturation} {self.lightness})"
        )

    def __str__(
        self,
    ):
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


ColorType = Union[RGBColor, HSVColor]
