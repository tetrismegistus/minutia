import random

import demos.display_maze as demos
from algorithms.mazes.recursive_backtracker import TrueRecursiveBacktracker
from algorithms.mazes.sidewinder import sidewinder
from common.grids.grid import Rectangle, Grid
from common.grids.masked_grid import MaskedGrid, MaskedDistanceGrid
from common.mask import Mask
from common.Animation import Animation
from common.downsample import downsample

# resolution = Rectangle(w=2560, h=1080)
# cell_size = Rectangle(w=3, h=3)
# grid_size = Grid.propose_grid_size(resolution=resolution, cell_size=cell_size)

# print(grid_size)
# demos.maze_without_walls(grid_size=grid_size, cell_size=cell_size, palette="winter", animation=False, png=True)
# demos.carve_and_flood(palette="winter")
# demos.compare_dead_ends()
# demos.deadend_map(palette="Greens")
# demos.depth_first_fill(grid_size=Rectangle(30, 30), animation=True, palette="hls")
# demos.find_long_path()
# demos.flood()
# mask = Mask.from_png('masks/jane.png')
# grid = MaskedDistanceGrid(mask, walls=True, palette="Reds")
# TrueRecursiveBacktracker(grid)
animation = Animation()
# grid.animation = animation
# path_start = grid.random_cell()
# grid.fill_distances(grid[path_start.row, path_start.column])
# grid.to_img(cell_size=Rectangle(10, 10)).save('brain.png')
# grid.animation.save_gif(reverse=True)

for x in range(1, 50):
    animation.frames = downsample('jane.jpg', sample_rate=x, shrink=False)

animation.save_gif(reverse=True)
# Todo: optimize gif size
# Todo: Create UI for generating and previewing and saving mazes, including serializing grid object
