from collections.abc import Mapping


class Distances(Mapping):
    def __init__(self, root):
        self.root = root
        self._cells = {self.root: 0}

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value

    def __iter__(self):
        return iter(self._cells)

    def __len__(self):
        return len(self._cells)

    def keys(self):
        return self._cells.keys()

    def path_to(self, goal):
        current = goal
        breadcrumbs = Distances(self.root)
        breadcrumbs[current] = self._cells[current]
        while current != self.root:
            for neighbor in current.links:
                if self._cells[neighbor] < self._cells[current]:
                    breadcrumbs[neighbor] = self._cells[neighbor]
                    current = neighbor
                    break
        return breadcrumbs

    def max(self):
        max_distance = 0
        max_cell = self.root
        for cell in self._cells:
            if self._cells[cell] > max_distance:
                max_cell = cell
                max_distance = self._cells[cell]
        return [max_cell, max_distance]
