"""
RGB Shifts provided image

Based on this tutorial:
http://datamoshing.com/2016/06/29/how-to-glitch-images-using-rgb-channel-shifting/
"""

__author__ = "Aric Maddux"
__version__ = "0.1.0"
__license__ = "Do whatever you want, I'm too depressed by the state of IP in this country to care license " \
              "(DWYWITDBTSOIITCTCL)"

import argparse
from random import randint

from PIL import Image


class RGBShift:
    def __init__(self, filename, iterations=5, recursiveIterations=False, shiftVertically=False,
                 shiftHorizontally=True, boundary=None):
        self.filename = filename
        self.iterations = iterations
        self.recursiveIterations = recursiveIterations
        self.shiftVertically = shiftVertically
        self.shiftHorizontally = shiftHorizontally
        self.source_img = Image.open(self.filename)
        self.w, self.h = self.source_img.size
        self.boundary = boundary if boundary else (0, 0, self.w, self.h)

    def retile_image(self):
        source_matrix = list(self.source_img.getdata())
        target_matrix = list(self.source_img.getdata())

        for i in range(self.iterations):
            # Channels to swap
            source_channel = randint(0, 2)
            target_channel = randint(0, 2)

            start_x = randint(0, self.w - 1)
            start_y = randint(0, self.h - 1)
            end_x = randint(start_x, self.w - 1)
            end_y = randint(start_y, self.h - 1)

            self.boundary = (start_x, start_y, end_x, end_y)

            horizontal_shift = randint(0, self.w) if self.shiftHorizontally else 0
            vertical_shift = randint(0, self.h) if self.shiftVertically else 0

            self.copy_box(source_matrix, target_matrix, vertical_shift, horizontal_shift)

            if self.recursiveIterations:
                source_matrix = target_matrix

        new_image = Image.new(self.source_img.mode, self.source_img.size)
        new_image.putdata(target_matrix)
        new_image.save('retiled' + self.filename)

    def copy_box(self, source_matrix, dest_matrix, source_y, source_x):
        for ydx in range(self.boundary[1], self.boundary[3]):
            source_y_offset = source_y + ydx
            if source_y_offset >= self.h:
                source_y_offset -= self.h
            for xdx in range(self.boundary[0], self.boundary[2], 3):
                source_x_offset = source_x + xdx
                if source_x_offset >= self.w:
                    source_x_offset -= self.w
                source_pixel = source_matrix[source_y_offset * self.w + source_x_offset]
                target_pixel = dest_matrix[ydx * self.w + xdx]

                dest_matrix[ydx * self.w + xdx] = source_pixel
                dest_matrix[source_y_offset * self.w + source_x_offset] = target_pixel


def add_bool_arg(parser, name, default=False):
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--' + name, dest=name, action='store_true')
    group.add_argument('--no-' + name, dest=name, action='store_false')

    parser.set_defaults(**{name: default})


def main(args):
    shift = RGBShift(args.file, iterations=args.i, recursiveIterations=args.recursive, shiftHorizontally=args.hshift,
                     shiftVertically=args.vshift, boundary=args.boundary)
    shift.retile_image()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("file", help="Filename to process")
    parser.add_argument("-i", help="Number of iterations", type=int, nargs='?', default=3)
    parser.add_argument('--boundary', nargs=4, type=int, default=None)
    add_bool_arg(parser, 'recursive')
    add_bool_arg(parser, 'hshift')
    add_bool_arg(parser, 'vshift')
    parser.set_defaults(hshift=True)

    arguments = parser.parse_args()
    main(arguments)
