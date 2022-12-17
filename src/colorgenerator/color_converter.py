from color import RGBColor, HSLColor, HSVColor


def __RGB_to_Hue(var_R, var_G, var_B, var_min, var_max):
    """
    For RGB_to_HSL and RGB_to_HSV, the Hue (H) component is calculated in
    the same way.
    """
    if var_max == var_min:
        return 0.0
    elif var_max == var_R:
        return (60.0 * ((var_G - var_B) / (var_max - var_min)) + 360) % 360.0
    elif var_max == var_G:
        return 60.0 * ((var_B - var_R) / (var_max - var_min)) + 120
    elif var_max == var_B:
        return 60.0 * ((var_R - var_G) / (var_max - var_min)) + 240.0


def RGB_to_HSV(color_obj: RGBColor):
    """
    Converts from RGB to HSV.

    H values are in degrees and are 0 to 360.
    S values are a percentage, 0.0 to 1.0.
    V values are a percentage, 0.0 to 1.0.
    """
    var_R = color_obj.red
    var_G = color_obj.green
    var_B = color_obj.blue

    var_max = max(var_R, var_G, var_B)
    var_min = min(var_R, var_G, var_B)

    var_H = __RGB_to_Hue(var_R, var_G, var_B, var_min, var_max)

    if var_max == 0:
        var_S = 0
    else:
        var_S = 1.0 - (var_min / var_max)

    var_V = var_max

    return HSVColor(var_H, var_S, var_V)


def RGB_to_HSL(color_obj: RGBColor):
    """
    Converts from RGB to HSL.

    H values are in degrees and are 0 to 360.
    S values are a percentage, 0.0 to 1.0.
    L values are a percentage, 0.0 to 1.0.
    """
    var_R = color_obj.red
    var_G = color_obj.green
    var_B = color_obj.blue

    var_max = max(var_R, var_G, var_B)
    var_min = min(var_R, var_G, var_B)

    var_H = __RGB_to_Hue(var_R, var_G, var_B, var_min, var_max)
    var_L = 0.5 * (var_max + var_min)

    if var_max == var_min:
        var_S = 0
    elif var_L <= 0.5:
        var_S = (var_max - var_min) / (2.0 * var_L)
    else:
        var_S = (var_max - var_min) / (2.0 - (2.0 * var_L))

    return HSLColor(var_H, var_S, var_L)

def HSV_to_RGB(color_obj: HSVColor) -> RGBColor:
    pass
