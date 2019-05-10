from random import randint
from collections import namedtuple

from PIL import Image, ImageColor, ImageDraw

from common.cell import Cell

Rectangle = namedtuple('rectangle', ['w', 'h'])


class Grid:
    def __init__(self, size: Rectangle):
        self.rows = size.h
        self.columns = size.w
        self.grid = self.prepare_grid()
        self.size = self.rows * self.columns
        self.configure_cells()

    def __getitem__(self, tup):
        row, col = tup
        vrow = row in range(0, self.rows)
        vcol = col in range(0, len(self.grid[row - 1]))
        return self.grid[row][col] if vrow and vcol else None

    def __str__(self):
        output = "grid.__str__ was mangled beyond recognition and requires a complete refactor"

        return output

    def contents_of(self, cell):
        return " "

    def background_color_for(self, cell):
        return (0, 0, 0, 0)

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
                if cell:
                    yield cell

    def dead_ends(self):
        return [cell for cell in self.each_cell() if len(cell.links) == 1]

    def to_img(self, cell_size: Rectangle = Rectangle(w = 10, h = 10), backgrounds=True, walls=True,
               background_color=(0, 0, 0, 0), wall_color='#FFFFFF'):
        img_h = int(cell_size.h * self.columns)
        img_w = int(cell_size.w * self.rows)
        margin = 1

        background = background_color
        wall_color = wall_color
        img = Image.new('RGBA', (img_w + margin, img_h + margin), color=background)
        modes = []
        if backgrounds:
            modes.append('backgrounds')

        if walls:
            modes.append('walls')

        drawing = ImageDraw.Draw(img)
        for mode in modes:
            for cell in self.each_cell():

                y1 = cell.column * cell_size.h  # northwest corner
                x1 = cell.row * cell_size.w
                y2 = (cell.column + 1) * cell_size.h  # southeast corner
                x2 = (cell.row + 1) * cell_size.w

                if mode == 'backgrounds':
                    color = self.background_color_for(cell)
                    if not color:
                        color = '#000000'
                    drawing.rectangle([(x1, y1), (x2, y2)], fill=color)
                else:
                    if not cell.west:
                        drawing.line([(x1, y1), (x2, y1)], fill=wall_color)

                    if not cell.north:
                        drawing.line([(x1, y1), (x1, y2)], fill=wall_color)

                    if not cell.linked(cell.south):
                        drawing.line([(x2, y1), (x2, y2)], fill=wall_color)

                    if not cell.linked(cell.east):
                        drawing.line([(x1, y2), (x2, y2)], fill=wall_color)
        return img

    @staticmethod
    def propose_cell_size(resolution: Rectangle, grid_size: Rectangle):
        height_cell_size = int(resolution.h / grid_size.h)
        width_cell_size = int(resolution.w / grid_size.w)
        return Rectangle(w=width_cell_size, h=height_cell_size)

    @staticmethod
    def propose_grid_size(resolution: Rectangle, cell_size: Rectangle):
        return Grid.propose_cell_size(resolution=resolution, grid_size=cell_size)
