from common.grids import distance, grid
from common.Animation import Animation
import common.runtimedefs as rundefs
from common.grids.grid import Rectangle, Grid

"""
animated gif notes:
larger mazes make huge files with a slowish animation 
post production mitigation currently done as

gifsicle --colors=255 animated.gif -o output.gif                        | prepare for frame removal
gifsicle -U output.gif `seq -f "#%g" 0 2 1000` -O2 -o output2.gif       | remove frames, can run multiple times
                                                                        | in this example 1000 is num of frames                                                                         
gifsicle -O3 < fast.gif fast2.gif                                       | further compression

"""


def find_long_path(grid_size: Rectangle = Rectangle(w = 20, h = 20), algo=rundefs.DEFAULTALGO,
                   cell_size: Rectangle = Rectangle(w = 10, h = 10),
                   palette="winter", walls=True, animation=False):
    if animation:
        animation = Animation()

    m = distance.XRayDistanceGrid(grid_size, palette=palette, cell_size=cell_size, walls=walls)
    m = algo(m)

    if animation:
        m.animation = animation

    path_start = m.random_cell()
    m.fill_distances(m[path_start.column, path_start.row])

    new_start, new_distance = m.distances.max()
    m.fill_distances(m[new_start.column, new_start.row])

    goal, new_distance = m.distances.max()
    m.distances = m.distances.path_to(goal)
    m.to_img(cell_size=cell_size).save(rundefs.DIRS['output'] + 'long_path.png', walls=walls)
    if animation:
        m.animation.save_gif()


def flood(grid_size: Rectangle = Rectangle(w=50, h=50), palette="winter", animation=True, png=False,
          algo=rundefs.DEFAULTALGO, cell_size: Rectangle = Rectangle(w=10, h=10),
          walls=True):
    if animation:
        animation = Animation()

    m = distance.XRayDistanceGrid(grid_size, palette=palette, walls=walls, cell_size=cell_size)
    m = algo(m)

    if animation:
        m.animation = animation

    m.fill_distances(m.random_cell())

    if animation:
        m.animation.save_gif()

    if png:
        m.to_img(cell_size=cell_size, walls=walls).save(rundefs.DIRS['output'] + 'flood.png')


def carve_and_flood(grid_size: Rectangle = Rectangle(w=20, h=20), palette="winter", algo=rundefs.DEFAULTALGO):
    animation = Animation()
    m = distance.XRayDistanceGrid(grid_size, palette=palette)
    m = algo(m, animation=animation)
    m.animation = animation
    m.fill_distances(m.random_cell())
    m.animation.save_gif()


def maze_without_walls(grid_size: Rectangle = Rectangle(w=50, h=50),
                       animation=True, png=False, palette="cubehelix",
                       algo=rundefs.DEFAULTALGO,
                       cell_size: Rectangle = Rectangle(w = 3, h = 3)):
    flood(grid_size, animation=animation, png=png, palette=palette, algo=algo, cell_size=cell_size, walls=False)


def plain_jane(grid_size: Rectangle, algo=rundefs.DEFAULTALGO, cell_size: Rectangle = Rectangle(w=10, h=10)):
    m = grid.Grid(grid_size)
    m = algo(m)
    m.to_img(cell_size=cell_size).save(rundefs.DIRS['output'] + 'plainjane.png')
