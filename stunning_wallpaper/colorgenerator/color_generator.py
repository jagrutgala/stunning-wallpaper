from abc import ABC, abstractmethod
import random
import sys
from typing import List, Optional, Tuple
from colorgenerator.color import ColorType, RGBColor, HSVColor
from colorgenerator.color_converter import ColorConverter


class ColorStrategy(ABC):
    @abstractmethod
    def getColors(self) -> List[HSVColor]:
        ...


class StaticColorStrategy(ColorStrategy):
    def __init__(self, colors: List[HSVColor]) -> None:
        self.colors = colors

    def getColors(self) -> List[HSVColor]:
        return self.colors


class AnalogousColorStrategy(ColorStrategy):
    """generates n random colors based on the base color using analogous algorithm"""

    MAX_HUE_SHIFT = HSVColor.MAX_HUE_VALUE
    MAX_SAT_SHIFT = HSVColor.MAX_SATURATION_VALUE
    MAX_VAL_SHIFT = HSVColor.MAX_VALUE_VALUE

    def __init__(
        self,
        color: HSVColor,
        color_count: int,
        hue_shift: float = 20,
        sat_shift: float = 10,
        val_shift: float = 10,
        seed: Optional[int] = None,
    ) -> None:
        """
        [hue_shift]: float = 0 <-> 100
        [sat_shift]: float = 0 <-> 100
        [val_shift]: float = 0 <-> 100
        """

        self.base_color = color
        self.color_count = color_count
        self.hue_shift = min(hue_shift * 360 / 100, self.MAX_HUE_SHIFT)
        self.sat_shift = min(sat_shift / 100, self.MAX_SAT_SHIFT)
        self.val_shift = min(val_shift / 100, self.MAX_VAL_SHIFT)
        if seed is None:
            seed = random.randrange(sys.maxsize)
        self.seed = seed

    def getColors(self) -> List[HSVColor]:
        hue, saturation, value = (
            self.base_color.hue,
            self.base_color.saturation,
            self.base_color.value,
        )

        random.seed(self.seed)
        color_list: List[HSVColor] = []
        for _ in range(self.color_count):
            tmp_hue = hue + random.uniform(-self.hue_shift // 2, self.hue_shift // 2)
            if tmp_hue > HSVColor.MAX_HUE_VALUE:
                tmp_hue = tmp_hue % HSVColor.MAX_HUE_VALUE

            tmp_sat = saturation + random.uniform(-self.sat_shift, self.sat_shift)
            tmp_sat = HSVColor.clamp_saturation(tmp_sat)

            tmp_val = value + random.uniform(-self.val_shift, self.val_shift)
            tmp_val = HSVColor.clamp_value(tmp_val)

            hsv_color_temp: HSVColor = HSVColor(
                round(tmp_hue),
                HSVColor.upscale_sat_val(tmp_sat),
                HSVColor.upscale_sat_val(tmp_val),
            )
            color_list.append(hsv_color_temp)
        return color_list


def generate_monochromatic_colors(color: RGBColor, color_count: int) -> List[RGBColor]:
    """"""
    ...


def generate_complementary_colors(color: RGBColor) -> RGBColor:
    """"""
    ...


def generate_square_colors(
    color: RGBColor,
) -> Tuple[RGBColor, RGBColor, RGBColor, RGBColor]:
    ...
