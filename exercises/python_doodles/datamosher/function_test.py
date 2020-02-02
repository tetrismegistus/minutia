from colorsys import rgb_to_hsv

from PIL import Image, ImageDraw


def rgb2int(r, g, b):
    return int('{:02x}{:02x}{:02x}'.format(r, g, b), 16)


def get_first_not_white_y(x, y, pixels, w, h, white_value):
    # expected 2314
    if y < h:
        while rgb2int(*pixels[x + y * w]) > white_value:
            y += 1
            if y >= h:
                return -1
    return y


def get_next_white_y(x, y, pixels, w, h, white_value):
    y += 1
    if y < h:
        while rgb2int(*pixels[x + y * w]) < white_value:
            y += 1
            if y >= h:
                return h - 1
    return y - 1


def get_first_not_black_y(x, y, pixels, w, h, black_value):
    if y < h:
        while rgb2int(*pixels[x + y * w]) < black_value:
            y += 1
            if y >= h:
                return -1
    return y


def get_next_black_y(x, y, pixels, w, h, black_value):
    y += 1
    if y < h:
        while rgb2int(*pixels[x + y * w]) > black_value:
            y += 1
            if y >= h:
                return -1

    return y - 1




white_value = 0x39A2C0
black_value = 0xbdc00
img = Image.open('fuzzed.jpg')
pixels = list(img.getdata())
w, h = img.size
for i in range(h):
    print(get_next_black_y(i, 0, pixels, w, h, black_value))     # expected 2314

# -5144191