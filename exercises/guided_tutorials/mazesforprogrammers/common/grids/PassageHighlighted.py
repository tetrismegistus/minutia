import numpy
import seaborn

from common.grids.grid import Rectangle, Grid


class DeadEndHighlighted(Grid):
    def __init__(self, size: Rectangle,
                 cell_size: Rectangle = Rectangle(w = 10, h = 10),
                 walls=True, palette='winter', animation=None):
        super(DeadEndHighlighted, self).__init__(size)
        self.palette = palette
        self.seaborn_palette = seaborn.color_palette(self.palette, 4).as_hex()
        print(len(self.seaborn_palette))
        self.animation = animation
        self.cell_size = cell_size
        self.walls = walls

    def background_color_for(self, cell):
        try:
            link_count = len(cell.links)
            if link_count == 0:
                return 'Gray'
            return self.seaborn_palette[link_count - 1]

        except TypeError:
            return super(DeadEndHighlighted, self).background_color_for(cell)
