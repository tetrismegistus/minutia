class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = {}
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def link(self, cell, bidi=True, animation=None, grid=None):
        self.links[cell] = True
        if animation:
            animation.frames = grid.to_img()
        if bidi:
            try:
                cell.link(self, False, animation=animation, grid=grid)
            except:
                print('links {} \ncell {}\n self {}'.format(self.links, cell, self))

        return animation

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

