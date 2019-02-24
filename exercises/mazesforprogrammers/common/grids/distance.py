import time
import os

import imageio
import numpy

from common.grids.grid import Grid
from common import runtimedefs as rd
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
    def background_color_for(self, cell):
        try:
            distance = self.distances.get(cell)
            distance = distance if distance else 0
            intensity = (self._maximum - distance) / self._maximum
            dark = round(255 * intensity)
            bright = 128 + round(127 * intensity)
            return dark, dark, bright
        except TypeError:
            return super(DistanceGrid, self).background_color_for(cell)


class AnimatedDistanceGrid(XRayDistanceGrid):
    def __init__(self, rows, columns):
        super(AnimatedDistanceGrid, self).__init__(rows, columns)
        for file_name in os.listdir(rd.DIRS['staging']):
            file_path = os.path.join(rd.DIRS['staging'], file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

    @property
    def distances(self):
        return self._distances

    @distances.setter
    def distances(self, distances):
        self._distances = distances
        farthest, self._maximum = distances.max()
        timestamp = time.time()
        img = self.to_img()
        img.save('{}{}.png'.format(rd.DIRS['staging'], timestamp))

    def save_gif(self):
        png_dir = rd.DIRS['staging']
        images = []
        for file_name in os.listdir(png_dir):
            if file_name.endswith('.png'):
                file_path = os.path.join(png_dir, file_name)
                images.append(imageio.imread(file_path))
        imageio.mimsave('{}animated.gif'.format(rd.DIRS['output']), images)