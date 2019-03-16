from algorithms.mazes.recursive_backtracker import TrueRecursiveBacktracker
from common.grids.grid import Rectangle
from common.grids.masked_grid import MaskedDistanceGrid
from common.mask import Mask
from common.Animation import Animation

# resolution = Rectangle(w=2560, h=1080)
# cell_size = Rectangle(w=3, h=3)
# grid_size = Grid.propose_grid_size(resolution=resolution, cell_size=cell_size)

mask = Mask.from_png('masks/jane.png')
grid = MaskedDistanceGrid(mask, walls=True, palette="Reds")
TrueRecursiveBacktracker(grid)
animation = Animation()
grid.animation = animation
path_start = grid.random_cell()
grid.fill_distances(grid[path_start.row, path_start.column])
grid.to_img(cell_size=Rectangle(10, 10)).save('brain.png')
grid.animation.save_gif(reverse=True)

# Todo: optimize gif size
# Todo: Create UI for generating and previewing and saving mazes, including serializing grid object
