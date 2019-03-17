from random import randint

from PIL import Image
from common.grids.grid import Rectangle


class Mask:
    def __init__(self, grid_size: Rectangle):
        self.rows = grid_size.w
        self.cols = grid_size.h
        self.bits = [[None for c in range(self.cols)] for r in range(self.rows)]
        self.states = []

    def __getitem__(self, tup):
        row, col = tup
        vrow = row in range(0, self.rows)
        vcol = col in range(0, len(self.bits[row - 1]))
        return self.bits[row][col] if vrow and vcol else False

    def __setitem__(self, tup, state):
        row, col = tup
        self.bits[row][col] = state

    def __iter__(self):
        for r in self.bits:
            yield r

    def count_enabled_bits(self):
        return sum([r.count(True) for r in self.bits])

    def get_random_enabled_bit(self, value=None):
        # will only ever return an enabled bit
        while True:
            row = randint(0, self.rows - 1)
            col = randint(0, self.cols - 1)
            if value:
                if self[row, col] and self[row, col] == value:
                    return row, col
            else:
                if self[row, col]:
                    return row, col

    def each_row(self):
        for row in range(self.rows):
            yield self.bits[row]

    def each_bit(self):
        for row in self.each_row():
            for bit in row:
                if bit:
                    yield bit

    @staticmethod
    def from_text_file(file):
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            while len(lines[-1]) < 1:
                lines.pop()

            rows = len(lines)
            cols = len(lines[0])
            mask = Mask(Rectangle(rows, cols))

            for row in range(mask.rows):
                for col in range(mask.cols):
                    if lines[row][col] == "X":
                        mask[row, col] = False
                    else:
                        mask[row, col] = True

        return mask

    @staticmethod
    def from_png(file):
        image = Image.open(file)
        w, h = image.size
        mask = Mask(Rectangle(w, h))
        states = []
        for row in range(mask.rows):
            for col in range(mask.cols):
                if image.getpixel((row, col)) == 0:
                    mask[row, col] = False
                else:
                    pixel = image.getpixel((row, col))
                    hexval = Mask.rgb2hex(pixel[0], pixel[1], pixel[2])
                    states.append(hexval)
                    mask[row, col] = hexval

        states = list(set(states))
        mask.states = states
        return mask

    @staticmethod
    def rgb2hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

