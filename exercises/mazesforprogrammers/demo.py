import demos.display_maze as demos
from common.grids.grid import Rectangle, Grid

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
demos.flood()


# Todo: optimize gif size
# Todo: Create UI for generating and previewing and saving mazes, including serializing grid object
# Todo: go through and make sure all algorithms receive animation object

