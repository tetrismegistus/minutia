import seaborn

from common.grids.grid import Grid, Rectangle
from common.cell import Cell
from common.grids.distance import DistanceGrid


class MaskedGrid(Grid):
    def __init__(self, mask):
        self.mask = mask
        grid_size = Rectangle(w=mask.cols, h=mask.rows)
        super(MaskedGrid, self).__init__(grid_size)

    def prepare_grid(self):

        return [[Cell(r, c) if self.mask[r, c] else None for c in range(self.columns)]
                for r in range(self.rows)]

    def random_cell(self):
        row, col = self.mask.get_random_enabled_bit()
        return self[row, col]

    def size(self):
        return self.mask.count_enabled_bits()


class MaskedDistanceGrid(MaskedGrid, DistanceGrid):
    def __init__(self, mask,
                 cell_size: Rectangle = Rectangle(w=10, h=10),
                 walls=True, palette='winter', animation=None):
        super(MaskedDistanceGrid, self).__init__(mask)
        self._distances = {}
        self._maximum = None
        self.palette = palette
        self.seaborn_palette = seaborn.color_palette(self.palette, 1).as_hex()
        self.animation = animation
        self.cell_size = cell_size
        self.walls = walls