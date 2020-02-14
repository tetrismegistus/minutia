import enum
import argparse

import numpy as np

from PIL import Image, ImageDraw


class mode(enum.Enum):
    BLACK = 0
    BRIGHTNESS = 1
    WHITE = 2


class PixelSort:
    def __init__(self, infile_name, mode, iterations=1, black_value=777216, brightness_value=60,
                 white_value=3777216, columns=True, rows=True, boundary=None):
        # orig_white 3777216
        self.filename = infile_name
        self.img = Image.open(infile_name)
        self.mode = mode
        self.iterations = iterations
        self.black_value = black_value
        self.white_value = white_value
        self.brightness_value = brightness_value
        self.w, self.h = self.img.size
        self.columns = columns
        self.rows = rows
        self.boundary = boundary if boundary else (0, 0, self.w, self.h)

    def sort_pixels(self):
        for x in range(self.iterations):
            if self.columns:
                for column in range(self.boundary[0], self.boundary[2]):
                    pixels = self.sort_column(column)
                    self.img.putdata(pixels)
                print('Columns finished')

            if self.rows:
                for row in range(self.boundary[1], self.boundary[3]):
                    pixels = self.sort_row(row)
                    self.img.putdata(pixels)
                print('Rows finished')

        self.img.save('SORTED.png')

    def sort_row(self, row):
        y = row
        x = self.boundary[0]
        xend = 0
        pixels = np.array(self.img.getdata())

        while xend < self.boundary[2] - 1:
            if self.mode == mode.BLACK:
                x = self.get_first_not_black_x(x, y, pixels)
                xend = self.get_next_black_x(x, y, pixels)
            elif self.mode == mode.BRIGHTNESS:
                x = self.get_first_bright_x(x, y, pixels)
                xend = self.get_next_dark_x(x, y, pixels)
            elif self.mode == mode.WHITE:
                x = self.get_first_not_white_x(x, y, pixels)
                xend = self.get_next_white_x(x, y, pixels)

            if x < 0:
                break

            sort_length = xend - x
            unsorted = []

            for i in range(sort_length):
                unsorted.append(pixels[x + i + y * self.w])

            unsorted.sort()

            for i in range(sort_length):
                pixels[x + i + y * self.w] = unsorted[i]

            x = xend + 1
        return pixels

    def sort_column(self, column):
        x = column
        y = self.boundary[1]
        yend = 0
        pixels = np.array(self.img.getdata())--

        while yend < self.boundary[1] - 1:
            if self.mode == mode.BLACK:
                y = self.get_first_not_black_y(x, y, pixels)
                yend = self.get_next_black_y(x, y, pixels)
            elif self.mode == mode.BRIGHTNESS:
                y = self.get_first_bright_y(x, y, pixels)
                yend = self.get_next_dark_y(x, y, pixels)
            elif self.mode == mode.WHITE:
                y = self.get_first_not_white_y(x, y, pixels)
                yend = self.get_next_white_y(x, y, pixels)

            if y < 0:
                break

            sort_length = yend - y
            unsorted = []

            for i in range(sort_length):
                unsorted.append(pixels[x + (y + i) * self.w])

            unsorted.sort()

            for i in range(sort_length):
                pixels[x + (y + i) * self.w] = unsorted[i]

            y = yend + 1

        return pixels

    def get_next_white_y(self, x, y, pixels):
        y += 1
        if y < self.boundary[3]:
            while rgb2int(*pixels[x + y * self.w]) < self.white_value:
                y += 1
                if y >= self.boundary[3]:
                    return self.boundary[3] - 1
        return y - 1

    def get_next_black_y(self, x, y, pixels):
        y += 1
        if y < self.boundary[3]:
            while rgb2int(*pixels[x + y * self.w]) > self.black_value:
                y += 1
                if y >= self.boundary[3]:
                    return self.boundary[3] - 1

        return y - 1

    def get_first_not_white_y(self, x, y, pixels):
        if y < self.boundary[3]:
            while rgb2int(*pixels[x + y * self.w]) > self.white_value:
                y += 1
                if y >= self.boundary[3]:
                    return -1
        return y

    def get_first_not_black_y(self, x, y, pixels):
        if y < self.boundary[3]:
            while rgb2int(*pixels[x + y * self.w]) < self.black_value:
                y += 1
                if y >= self.boundary[3]:
                    return -1
        return y

    def get_next_dark_y(self, x, y, pixels):
        y += 1
        if y < self.boundary[3]:
            while self.brightness(pixels[x + y * self.w]) > self.brightness_value:
                y += 1
                if y >= self.boundary[3]:
                    return self.boundary[3] - 1
        return y - 1

    def get_first_bright_y(self, x, y, pixels):
        if y < self.boundary[3]:
            while self.brightness(pixels[x + y * self.w]) < self.brightness_value:
                y += 1
                if y >= self.boundary[3]:
                    return -1
        return y

    def get_next_white_x(self, x, y, pixels):
        x += 1
        while rgb2int(*pixels[x + y * self.w]) < self.white_value:
            x += 1
            if x >= self.boundary[2]:
                return self.boundary[2] - 1
        return x - 1

    def get_first_not_white_x(self, x, y, pixels):
        while rgb2int(*pixels[x + y * self.w]) > self.white_value:
            x += 1
            if x >= self.boundary[2]:
                return -1
        return x

    def get_next_dark_x(self, x, y, pixels):
        x += 1
        while self.brightness(pixels[x + y * self.w]) > self.brightness_value:
            x += 1
            if x >= self.boundary[2]:
                return self.boundary[2] - 1
        return x - 1

    def get_first_bright_x(self, x, y, pixels):
        while self.brightness(pixels[x + y * self.w]) < self.brightness_value:
            x += 1
            if x >= self.boundary[2]:
                return -1
        return x

    def get_next_black_x(self, x, y, pixels):
        x += 1
        while rgb2int(*pixels[x + y * self.w]) > self.black_value:
            x += 1
            if x >= self.boundary[2]:
                return self.boundary[2] - 1
        return x

    def get_first_not_black_x(self, x, y, pixels):
        while rgb2int(*pixels[x + y * self.w]) < self.black_value:
            x += 1
            if x >= self.boundary[2]:
                return -1
        return x

    def brightness(self, pixel):
        return max(pixel[0], pixel[1], pixel[2])


def rgb2int(r, g, b, a=None):
    return int('{:02x}{:02x}{:02x}'.format(r, g, b), 16)


def add_bool_arg(parser, name, default=False):
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--' + name, dest=name, action='store_true')
    group.add_argument('--no-' + name, dest=name, action='store_false')

    parser.set_defaults(**{name: default})


def main(args):
    modes = {"bright": mode.BRIGHTNESS,
             "black": mode.BLACK,
             "white": mode.WHITE}
    arg_mode = modes[args.mode]

    ps = PixelSort(args.file, arg_mode, white_value=args.w,  black_value=args.b,
                   brightness_value=args.br, iterations=args.i, rows=args.rows, columns=args.columns,
                   boundary=args.boundary)
    ps.sort_pixels()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("file", help="Filename to process")
    parser.add_argument("-i", help="Number of iterations", type=int, nargs='?', default=1)
    parser.add_argument("-w", help="white value", type=int, default=3777216)
    parser.add_argument("-b", help="black value", type=int, default=777216)
    parser.add_argument("-br", help="brightness value", type=int, default=60)
    parser.add_argument("--mode", help="sort mode, [black], [white], [bright]", type=str, default="bright")
    parser.add_argument('--boundary', nargs=4, type=int, default=None)
    add_bool_arg(parser, 'rows')
    add_bool_arg(parser, 'columns')
    parser.set_defaults(rows=True)
    parser.set_defaults(columns=False)

    arguments = parser.parse_args()
    main(arguments)
