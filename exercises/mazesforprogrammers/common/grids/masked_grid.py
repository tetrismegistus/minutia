from PIL import Image
import seaborn


from common.grids.grid import Grid, Rectangle
from common.cell import Cell
from common.grids.distance import DistanceGrid


class MaskedGrid(Grid):
    def __init__(self, mask, state='#000000'):
        self.state = state
        self.mask = mask
        grid_size = Rectangle(w=mask.cols, h=mask.rows)
        super(MaskedGrid, self).__init__(grid_size)

    def prepare_grid(self):
        return [[Cell(r, c) if self.mask[r, c] == self.state else None for c in range(self.columns)]
                for r in range(self.rows)]

    def random_cell(self):
        while True:
            row, col = self.mask.get_random_enabled_bit(value=self.state)
            return self[row, col]

    def size(self):
        return self.mask.count_enabled_bits()


class MaskedDistanceGrid(MaskedGrid, DistanceGrid):
    def __init__(self, mask, state='#000000',
                 cell_size: Rectangle = Rectangle(w=10, h=10),
                 walls=True, palette='winter', animation=None):
        super(MaskedDistanceGrid, self).__init__(mask, state=state)
        self._distances = {}
        self._maximum = None
        self.palette = palette
        self.seaborn_palette = seaborn.color_palette(self.palette, 1).as_hex()
        self.animation = animation
        self.cell_size = cell_size
        self.walls = walls

    def background_color_for(self, cell):
        try:
            if len(cell.links) == 0:
                return 'Gray'
            distance = self.distances.get(cell)
            return self.seaborn_palette[distance]
        except TypeError:
            return super(DistanceGrid, self).background_color_for(cell)


class MultiStateMaskedDistanceGrid:
    def __init__(self, mask, state_table):
        self.mask = mask
        self.grid_size = Rectangle(w=mask.cols, h=mask.rows)
        self.state_table = state_table
        self.grids = {}
        self.make_grids()
        self.carve_grids()
        self.fill_grids()

    def make_grids(self):
        for state in self.mask.states:
            self.grids[state] = MaskedDistanceGrid(self.mask, walls=self.state_table[state][2], state=state,
                                                   palette=self.state_table[state][1])

    def carve_grids(self):
        for state in self.mask.states:
            algo = self.state_table[state][0]
            algo(self.grids[state])

    def fill_grids(self):
        for state in self.mask.states:
            row, col = self.mask.get_random_enabled_bit(value=state)
            self.grids[state].fill_distances(self.grids[state][row, col])

    def to_img(self, filename):
        images = []
        for state in self.mask.states:
            images.append(self.grids[state].to_img())

        combined = Image.new("RGBA", images[0].size)
        for image in images:
            combined = Image.alpha_composite(combined, image)
        combined.save(filename)


