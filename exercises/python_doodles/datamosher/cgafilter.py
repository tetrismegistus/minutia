import numpy as np
from PIL import Image
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

COLORS = {'CYAN': np.array((96, 167, 169)),
          'MAGENTA': np.array((146, 40, 167)),
          'GRAY': np.array((170, 170, 170)),
          'LIGHTCYAN': np.array((161, 251, 254)),
          'LIGHTMAGENTA': np.array((224, 104, 251)),
          'WHITE': np.array((255, 255, 255))}

LABCOLORS = {'CYAN': convert_color(sRGBColor(96, 167, 169), LabColor),
             'MAGENTA': convert_color(sRGBColor(146, 40, 167), LabColor),
             'GRAY': convert_color(sRGBColor(170, 170, 170), LabColor),
             'LIGHTCYAN': convert_color(sRGBColor(161, 251, 254), LabColor),
             'LIGHTMAGENTA': convert_color(sRGBColor(224, 104, 251), LabColor),
             'WHITE': convert_color(sRGBColor(255, 255, 255), LabColor)}


def update_pixel(p):
    color = convert_color(sRGBColor(p[0], p[1], p[2]), LabColor)
    distance = None
    return_color = None

    for k, v in LABCOLORS.items():
        delta = delta_e_cie2000(color, v)
        if distance is None or delta < distance:
            distance = delta
            return_color = COLORS[k]
    return return_color


source_img = Image.open('bjork.jpg')
source_arr = np.array(source_img)

new_img = np.apply_along_axis(update_pixel, 2, source_arr)
new_pil_img = Image.fromarray(new_img.astype(np.uint8))
new_pil_img.save('testcga.png')
