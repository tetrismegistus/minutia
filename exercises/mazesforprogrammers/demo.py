import demos.display_maze as demo
from common.grids.grid import Rectangle, Grid

resolution = Rectangle(w=1680, h=1050)
cell_size = Rectangle(w=3, h=3)
grid_size = Grid.propose_grid_size(resolution=resolution, cell_size=cell_size)
print(grid_size)

demo.maze_without_walls(grid_size, animation=False, png=True, cell_size=cell_size, palette="winter")

# Todo: optimize gif size
# Todo: Create UI for generating and previewing and saving mazes, including serializing grid object
# Todo: go through and make sure all algorithms receive animation object

