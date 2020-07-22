from mazesvg.common.grids import grid, distance
from mazesvg.common.grids.grid import Rectangle
from mazesvg.algorithms.mazes.wilsons import wilsons


def plain_jane(grid_size: Rectangle, algo=wilsons,
               cell_size: Rectangle = Rectangle(w=10, h=10)):
    m = grid.Grid(grid_size)
    algo(m)
    m.to_img(cell_size=cell_size, filename='plainjane.svg')


def find_long_path(grid_size: Rectangle = Rectangle(w=50, h=50), algo=wilsons,
                   cell_size: Rectangle = Rectangle(w=10, h=10), walls=True):

    m = distance.DistanceGrid(grid_size, cell_size=cell_size, walls=walls)

    algo(m)

    path_start = m.random_cell()
    m.fill_distances(m[path_start.column, path_start.row])

    new_start, new_distance = m.distances.max()
    m.fill_distances(m[new_start.column, new_start.row])

    goal, new_distance = m.distances.max()
    m.distances = m.distances.path_to(goal)

    return m


m = find_long_path()
m.to_img(filename='path2.svg')