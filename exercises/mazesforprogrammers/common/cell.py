from algorithms.pathfinders.distances import Distances


class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = {}
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            try:
                cell.link(self, False)
            except:
                print('links {} \ncell {}\n self {}'.format(self.links, cell, self))

    def unlink(self, cell, bidi=True):
        del self.links[cell]
        if bidi:
            cell.unlink(self, False)

    def links(self):
        return self.links.keys()

    def linked(self, cell):
        return True if self.links.get(cell) else False

    def neighbors(self):
        dlist = []
        for direction in [self.north, self.south, self.east, self.west]:
            if direction:
                dlist.append(direction)
        return dlist

