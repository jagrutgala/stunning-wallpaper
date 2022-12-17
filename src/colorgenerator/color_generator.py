from typing import List, Tuple
from color import RGBColor, HSVColor
from color_converter import RGB_to_HSV, RGB_to_HSL, HSV_to_RGB


def generate_analogous_colors(color: RGBColor, color_count: int, hue_shift: int = 30) -> List[RGBColor]:
    hsv_color: HSVColor = RGB_to_HSV(color)
    color_list: List[RGBColor] = []
    # 5 -> (-2, -1, 0, 1, 2) : count = 5
    # 4 -> (-2, -1, 1, 2) : count = 4
    for i in range(color_count // 2):
        hsv_color_temp: HSVColor = HSVColor(
            hsv_color.hue + (i * hue_shift), hsv_color.saturation, hsv_color.brightness)
        color_list.append(
            HSV_to_RGB(hsv_color_temp)
        )


def generate_monochromatic_colors(color: RGBColor, color_count: int) -> List[RGBColor]:
    hsv_color: HSVColor = RGB_to_HSV(color)


def generate_complementary_colors(color: RGBColor) -> RGBColor:
    """
    Input: color: RGBColor
    Returns the complementary color.
    """
    complementart_color = RGBColor(
        RGBColor.MAX_COORD_VALUE - color.red,
        RGBColor.MAX_COORD_VALUE - color.green,
        RGBColor.MAX_COORD_VALUE - color.blue
    )
    return complementart_color


def generate_square_colors(color: RGBColor) -> Tuple[RGBColor, RGBColor, RGBColor, RGBColor]:
    pass
