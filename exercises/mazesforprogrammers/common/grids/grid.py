from random import randint

from PIL import Image, ImageColor, ImageDraw

from common.cell import Cell


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.size = rows * columns
        self.configure_cells()

    def __getitem__(self, tup):
        row, col = tup
        vrow = row in range(0, self.rows)
        vcol = col in range(0, len(self.grid[row - 1]))
        return self.grid[row][col] if vrow and vcol else None

    def __str__(self):
        # God forgive me
        output = ""
        for rindex, row in enumerate(self.each_row()):
            # for every row of the grid
            if rindex == 0:
                # draw top row
                output += "┏"
                for cindex, col in enumerate(row):
                    # for every cell of the top row draw the top wall
                    output += "━━━"
                    # and an appropriate corner
                    if col.linked(col.east):
                        output += "━"
                    elif cindex == self.columns - 1:
                        output += "┓"
                    else:
                        output += "┳"
                output += "\n"

            cell_row = ""
            bottom_row = ""
            for cindex, col in enumerate(row):
                if cindex == 0:
                    cell_row += "┃"
                    if rindex == self.rows - 1:
                        bottom_row += "┗"
                    else:
                        bottom_row += "┃" if col.linked(col.south) else "┣"

                # entries represent whether there is a connecting wall at that dir from corner
                # 'n': False   ==   there is no connecting wall to the north
                # all corners are the southeast corner of the current cell, or col
                bottom_corner = {'n': False if col.linked(col.east) else True,
                                 'e': None,
                                 's': None,
                                 'w': False if col.linked(col.south) else True}

                if col.east:
                    bottom_corner['e'] = False if col.east.linked(col.east.south) else True
                else:
                    bottom_corner['e'] = False

                if col.south:
                    bottom_corner['s'] = False if col.south.linked(col.south.east) else True
                else:
                    bottom_corner['s'] = False

                cell_contents = self.contents_of(col)

                cell_row += '{}'.format(self.contents_of(col)).rjust(3)
                cell_row += " " if col.linked(col.east) else "┃"
                cell_row += "\n" if cindex == self.rows - 1 else ""

                if (bottom_corner['n'] and
                        bottom_corner['s'] and
                        bottom_corner['e'] and
                        bottom_corner['w']):
                    corner = "╋"
                elif (bottom_corner['n'] and
                        bottom_corner['e'] and
                        bottom_corner['w'] and
                        not bottom_corner['s']):
                    corner = "┻"
                elif (bottom_corner['n'] and
                        bottom_corner['e'] and
                        bottom_corner['s']):
                    corner = "┣"
                elif (bottom_corner['n'] and
                        bottom_corner['w'] and
                        bottom_corner['s']):
                    corner = "┫"
                elif (bottom_corner['s'] and
                        bottom_corner['e'] and
                        bottom_corner['w']):
                    corner = "┳"
                elif (bottom_corner['n'] and
                      bottom_corner['s']):
                    corner = "┃"
                elif (bottom_corner['e'] and
                      bottom_corner['w']):
                    corner = "━"
                elif (bottom_corner['w'] and
                      bottom_corner['s']):
                    corner = "┓"
                elif (bottom_corner['e'] and
                      bottom_corner['s']):
                    corner = "┏"
                elif (bottom_corner['e'] and
                      bottom_corner['n']):
                    corner = "┗"
                elif (bottom_corner['w'] and
                      bottom_corner['n']):
                    corner = "┛"
                elif bottom_corner['w']:
                    corner = "╸"
                elif bottom_corner['e']:
                    corner = "╺"
                elif bottom_corner['s']:
                    corner = "┃"

                bottom_row += "   " if col.linked(col.south) else "━━━"
                bottom_row += corner

                # draw right
            output += cell_row + bottom_row + "\n"

        return output

    def contents_of(self, cell):
        return " "

    def background_color_for(self, cell):
        return None

    def prepare_grid(self):
        return [[Cell(r, c) for c in range(self.columns)] for r in range(self.rows)]

    def configure_cells(self):
        for cell in self.each_cell():
            row, col = cell.row, cell.column
            cell.north = self[row - 1, col]
            cell.south = self[row + 1, col]
            cell.west = self[row, col - 1]
            cell.east = self[row, col + 1]

    def random_cell(self):
        row = randint(0, self.rows - 1)
        col = randint(0, len(self.grid[row]) - 1)
        return self[row, col]

    def size(self):
        return self.rows * self.columns

    def each_row(self):
        for row in range(self.rows):
            yield self.grid[row]

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell

    def to_img(self, cell_size=10, backgrounds=True, walls=True):
        img_w = int(cell_size * self.columns)
        img_h = int(cell_size * self.rows)
        margin = 1

        background = ImageColor.getcolor('White', 'RGB')
        wall = ImageColor.getcolor('Black', 'RGB')
        img = Image.new('RGB', (img_w + margin, img_h + margin), color=background)
        modes = []
        if backgrounds:
            modes.append('backgrounds')

        if walls:
            modes.append('walls')

        drawing = ImageDraw.Draw(img)
        for mode in modes:
            for cell in self.each_cell():
                x1 = cell.column * cell_size  # northwest corner
                y1 = cell.row * cell_size
                x2 = (cell.column + 1) * cell_size  # southeast corner
                y2 = (cell.row + 1) * cell_size

                if mode == 'backgrounds':
                    color = self.background_color_for(cell)
                    drawing.rectangle([(x1, y1), (x2, y2)], fill=color if color else None)
                else:
                    if not cell.north:
                        drawing.line([(x1, y1), (x2, y1)], fill=wall)

                    if not cell.west:
                        drawing.line([(x1, y1), (x1, y2)], fill=wall)

                    if not cell.linked(cell.east):
                        drawing.line([(x2, y1), (x2, y2)], fill=wall)

                    if not cell.linked(cell.south):
                        drawing.line([(x1, y2), (x2, y2)], fill=wall)
        return img


