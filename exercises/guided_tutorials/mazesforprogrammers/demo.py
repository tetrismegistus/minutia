from algorithms.mazes.recursive_backtracker import TrueRecursiveBacktracker
from common.grids.grid import Rectangle
from common.grids.masked_grid import MaskedDistanceGrid, MultiStateMaskedDistanceGrid
from common.mask import Mask
from common.Animation import Animation
from demos import display_maze
from common.runtimedefs import STATE_LOOKUP, DIRS

# resolution = Rectangle(w=2560, h=1080)
# cell_size = Rectangle(w=3, h=3)
# grid_size = Grid.propose_grid_size(resolution=resolution, cell_size=cell_size)
mask = Mask.from_png('masks/heather_maze.png')
m = MultiStateMaskedDistanceGrid(mask, state_table=STATE_LOOKUP)
m.to_img(DIRS['output'] + 'multi.png')

# Todo: optimize gif size
# Todo: Create UI for generating and previewing and saving mazes, including serializing grid object
