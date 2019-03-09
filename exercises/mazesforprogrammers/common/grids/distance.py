import numpy
import seaborn

from common.grids.grid import Grid
from algorithms.pathfinders.distances import Distances


class DistanceGrid(Grid):
    def __init__(self, rows, columns):
        super(DistanceGrid, self).__init__(rows, columns)
        self._distances = {}
        self._maximum = None

    @property
    def distances(self):
        return self._distances

    @distances.setter
    def distances(self, distances):
        self._distances = distances
        farthest, self._maximum = distances.max()

    def contents_of(self, cell):
        if self.distances and self.distances.get(cell) is not None:
            return '{}'.format(numpy.base_repr(self.distances[cell], 36))
        else:
            return super(DistanceGrid, self).contents_of(cell)

    def fill_distances(self, cell):
        distances = Distances(cell)
        frontier = [cell]
        while True:
            new_frontier = []
            for c in frontier:
                for linked in c.links:
                    if distances.get(linked) is not None:
                        continue
                    distances[linked] = distances[c] + 1
                    new_frontier.append(linked)
            self.distances = distances
            frontier = new_frontier
            if len(frontier) == 0:
                break


class XRayDistanceGrid(DistanceGrid):
    def __init__(self, rows, columns, cell_size=10, walls=True, palette='winter', animation=None):
        super(XRayDistanceGrid, self).__init__(rows, columns)
        self.palette = palette
        self.seaborn_palette = seaborn.color_palette(self.palette, 1).as_hex()
        self.animation = None
        self.cell_size = cell_size
        self.walls = walls

    @property
    def distances(self):
        return self._distances

    @distances.setter
    def distances(self, distances):
        self._distances = distances
        farthest, self._maximum = distances.max()
        tones = self._maximum if self._maximum else 0
        # self.seaborn_palette = seaborn.dark_palette("purple", tones + 1).as_hex()
        self.seaborn_palette = seaborn.color_palette(self.palette, tones + 1).as_hex()
        if self.animation:
            self.animation.frames = self.to_img(cell_size=self.cell_size, walls=self.walls)

    def background_color_for(self, cell):
        try:
            distance = self.distances.get(cell)
            return self.seaborn_palette[distance]
        except TypeError:
            return super(DistanceGrid, self).background_color_for(cell)