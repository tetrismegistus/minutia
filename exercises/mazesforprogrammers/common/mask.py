from random import randint

from PIL import Image
from common.grids.grid import Rectangle


class Mask:
    def __init__(self, grid_size: Rectangle):
        self.rows = grid_size.w
        self.cols = grid_size.h
        self.bits = [[True for c in range(self.cols)] for r in range(self.rows)]

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

    def get_random_enabled_bit(self):
        # will only ever return an enabled bit
        while True:
            row = randint(0, self.rows - 1)
            col = randint(0, self.cols - 1)
            if self[row, col]:
                return row, col

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
        image = Image.open(file).convert("1")
        w, h = image.size
        mask = Mask(Rectangle(w, h))

        for row in range(mask.rows):
            for col in range(mask.cols):
                if image.getpixel((row, col)) == 0:
                    mask[row, col] = False
                else:
                    mask[row, col] = True

        return mask
