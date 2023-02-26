from typing import Any, Callable, Tuple, Type, TypeVar
from colorgenerator.color import RGBColor, HSLColor, HSVColor

T = TypeVar("T")

class ConversionError(Exception):
    pass


class ColorConverter:
    conversionMap: dict[Tuple[Any, Any], Callable[..., Any]] = dict()

    def convert(self, color_from, color_to_type: Type[T]) -> T:
        color_from_type= type(color_from)
        conversionFn = self.conversionMap.get((color_from_type, color_to_type), None)
        if conversionFn is None:
            raise ConversionError(
                f"Convertion from {color_from.__class__.__name__} to {color_to_type.__name__} is not regitered"
            )
        return conversionFn(color_from)

    @classmethod
    def register(cls, from_type: Type[Any], to_type: Type[T]):
        def conversion_wrapper(func: Callable[..., T]):
            cls.conversionMap.update({(from_type, to_type): func})
            def _wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return _wrapper
        return conversion_wrapper

@ColorConverter.register(HSVColor, RGBColor)
def hsv_to_rgb(hsv_color: HSVColor) -> RGBColor:
    hue, saturation, value = (hsv_color.hue, hsv_color.saturation, hsv_color.value)

    chroma = value * saturation
    hue_ = hue / 60.0
    x = chroma * (1 - abs(hue_ % 2 - 1))
    m = value - chroma
    r, g, b = 0, 0, 0
    if 0 <= hue_ < 1:
        r, g, b = chroma, x, 0
    elif 1 <= hue_ < 2:
        r, g, b = x, chroma, 0
    elif 2 <= hue_ < 3:
        r, g, b = 0, chroma, x
    elif 3 <= hue_ < 4:
        r, g, b = 0, x, chroma
    elif 4 <= hue_ < 5:
        r, g, b = x, 0, chroma
    else:
        r, g, b = chroma, 0, x

    red, green, blue = (r + m) * 255, (g + m) * 255, (b + m) * 255

    return RGBColor(round(red), round(green), round(blue))

@ColorConverter.register(HSLColor, RGBColor)
def hsl_to_rgb(hsl_color: HSLColor) -> RGBColor:
    """Convert HSL color to RGB color."""
    hue, saturation, lightness = (
        hsl_color.hue,
        hsl_color.saturation,
        hsl_color.lightness,
    )

    chroma = (1 - abs(2 * lightness - 1)) * saturation
    hue_prime = hue / 60
    x = chroma * (1 - abs(hue_prime % 2 - 1))
    red = green = blue = 0
    if 0 <= hue_prime < 1:
        red, green, blue = chroma, x, 0
    elif 1 <= hue_prime < 2:
        red, green, blue = x, chroma, 0
    elif 2 <= hue_prime < 3:
        red, green, blue = 0, chroma, x
    elif 3 <= hue_prime < 4:
        red, green, blue = 0, x, chroma
    elif 4 <= hue_prime < 5:
        red, green, blue = x, 0, chroma
    elif 5 <= hue_prime < 6:
        red, green, blue = chroma, 0, x
    m = lightness - chroma / 2
    red, green, blue = (red + m) * 255, (green + m) * 255, (blue + m) * 255

    return RGBColor(round(red), round(green), round(blue))

@ColorConverter.register(RGBColor, HSVColor)
def rgb_to_hsv(rgb_color: RGBColor) -> HSVColor:
    red, green, blue = rgb_color.red, rgb_color.green, rgb_color.blue

    min_val, max_val = min(red, green, blue), max(red, green, blue)
    delta_value = max_val - min_val
    hue = 0
    if delta_value != 0:
        if max_val == red:
            hue = ((green - blue) * 60) / delta_value % 360
        elif max_val == green:
            hue = ((blue - red) * 60) / delta_value + 120
        else:
            hue = ((red - green) * 60) / delta_value + 240
    saturation = 0
    if delta_value != 0:
        saturation = (delta_value / max_val) * 100
    value = max_val * 100

    return HSVColor(round(hue), round(saturation), round(value))

@ColorConverter.register(RGBColor, HSLColor)
def rgb_to_hsl(rgb_color: RGBColor) -> HSLColor:
    """Convert RGB color to HSL color."""

    red, green, blue = rgb_color.red, rgb_color.green, rgb_color.blue
    min_value, max_value = min(red, green, blue), max(red, green, blue)
    diff = max_value - min_value

    lightness = (max_value + min_value) / 2
    if diff == 0:
        return HSLColor(0, 0, round(lightness) * 100)

    saturation = diff / (1 - abs(2 * lightness - 1))
    if max_value == red:
        hue = (green - blue) / diff % 6
    elif max_value == green:
        hue = (blue - red) / diff + 2
    else:
        hue = (red - green) / diff + 4
    hue *= 60
    if hue < 0:
        hue += 360

    return HSLColor(round(hue), round(saturation * 100), round(lightness * 100))
