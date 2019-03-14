from operator import itemgetter
from collections import OrderedDict

from common.grids import distance, grid, PassageHighlighted
from common.Animation import Animation
import common.runtimedefs as rundefs
from common.grids.grid import Rectangle
from algorithms.mazes import aldous_broder, binary_tree, hunt_and_kill, wilsons, sidewinder, recursive_backtracker


"""
animated gif notes:
larger mazes make huge files with a slowish animation 
post production mitigation currently done as

gifsicle --colors=255 animated.gif -o output.gif                        | prepare for frame removal
gifsicle -U output.gif `seq -f "#%g" 0 2 1000` -O2 -o output2.gif       | remove frames, can run multiple times
                                                                        | in this example 1000 is num of frames                                                                         
gifsicle -O3 < fast.gif fast2.gif                                       | further compression

"""


def create_maze(grid_size, palette, cell_size, walls, grid, algo, animation, filename):
    m = grid(grid_size, palette=palette, cell_size=cell_size, walls=walls)

    algo(m)

    if animation:
        animation = Animation()
        m.animation = animation
    else:
        animation = False

    path_start = m.random_cell()
    m.fill_distances(m[path_start.column, path_start.row])

    m.to_img(cell_size=cell_size).save(rundefs.DIRS['output'] + filename, walls=walls)

    if animation:
        m.animation.save_gif()


def find_long_path(grid_size: Rectangle = Rectangle(w = 20, h = 20), algo=rundefs.DEFAULTALGO,
                   cell_size: Rectangle = Rectangle(w = 10, h = 10),
                   palette="winter", walls=True, animation=False, png=True):

    m = distance.DistanceGrid(grid_size, palette=palette, cell_size=cell_size, walls=walls)

    algo(m)

    if animation:
        animation = Animation()
        m.animation = animation
    else:
        animation = False

    path_start = m.random_cell()
    m.fill_distances(m[path_start.column, path_start.row])

    new_start, new_distance = m.distances.max()
    m.fill_distances(m[new_start.column, new_start.row])

    goal, new_distance = m.distances.max()
    m.distances = m.distances.path_to(goal)
    m.to_img(cell_size=cell_size).save(rundefs.DIRS['output'] + filename, walls=walls)

    if animation:
        m.animation.save_gif()


def depth_first_fill(grid_size: Rectangle = Rectangle(w=30, h=30), palette="winter", animation=True, png=False,
          algo=rundefs.DEFAULTALGO, cell_size: Rectangle = Rectangle(w=10, h=10),
          walls=True):

    create_maze(grid_size=grid_size, palette=palette, animation=animation, png=png, algo=algo, cell_size=cell_size,
                walls=walls, grid=distance.DepthFirstSearch, filename='depth_first.png')


def flood(grid_size: Rectangle = Rectangle(w=50, h=50), palette="winter", animation=True, png=False,
          algo=rundefs.DEFAULTALGO, cell_size: Rectangle = Rectangle(w=10, h=10),
          walls=True):

    create_maze(grid_size=grid_size, palette=palette, animation=animation, png=png, algo=algo, cell_size=cell_size,
                walls=walls, grid=distance.DistanceGrid, filename='flood.png')


def maze_without_walls(grid_size: Rectangle = Rectangle(w=50, h=50),
                       animation=True, png=False, palette="cubehelix",
                       algo=rundefs.DEFAULTALGO,
                       cell_size: Rectangle = Rectangle(w = 3, h = 3)):
    flood(grid_size, animation=animation, png=png, palette=palette, algo=algo, cell_size=cell_size, walls=False)


def carve_and_flood(grid_size: Rectangle = Rectangle(w=20, h=20), palette="winter", algo=rundefs.DEFAULTALGO):
    animation = Animation()
    m = distance.DistanceGrid(grid_size, palette=palette)
    algo(m, animation=animation)
    m.animation = animation
    m.fill_distances(m.random_cell())
    m.animation.save_gif()


def plain_jane(grid_size: Rectangle, algo=rundefs.DEFAULTALGO,
               cell_size: Rectangle = Rectangle(w=10, h=10), cprint=False):
    m = grid.Grid(grid_size)
    algo(m)
    m.to_img(cell_size=cell_size).save(rundefs.DIRS['output'] + 'plainjane.png')
    if cprint:
        print(m)


def deadend_map(grid_size: Rectangle = Rectangle(w = 50, h = 50),
                            cell_size: Rectangle = Rectangle(w = 10, h = 10),
                            walls: bool = True,
                            palette: str = "winter",
                            algo=rundefs.DEFAULTALGO):

    m = PassageHighlighted.DeadEndHighlighted(grid_size, cell_size=cell_size, walls=False, palette=palette)
    algo(m)
    m.to_img(cell_size=cell_size, walls=walls).save(rundefs.DIRS['output'] + 'deadends.png', walls=walls)


def compare_dead_ends(grid_size: Rectangle = Rectangle(w=20, h=20), tries: int = 100):
    algos = [aldous_broder.AldousBroder, wilsons.wilsons, binary_tree.binary_tree, sidewinder.sidewinder,
             hunt_and_kill.hunt_and_kill, recursive_backtracker.TrueRecursiveBacktracker]
    names = "aldous-broder wilsons binary_tree sidewinder hunt_and_kill recursive_backtracker".split()
    averages = {}

    for algo, name in zip(algos, names):
        print("Running {}".format(name))
        deadend_counts = []
        for t in range(tries):
            m = grid.Grid(grid_size)
            algo(m)
            deadend_counts.append(len(m.dead_ends()))
        total_deadends = sum(deadend_counts)
        averages[name] = total_deadends / len(deadend_counts)

    total_cells = grid_size.w * grid_size.h
    sorted_averages = OrderedDict(sorted(averages.items(), key=itemgetter(1)))

    print("Average dead-ends per {}x{} maze ({} cells): ".format(grid_size.w, grid_size.h, total_cells))
    for algorithm, average in sorted_averages.items():
        percentage = averages[algorithm] * 100.0 / (grid_size.w * grid_size.h)
        print("{} Average:\t {}/{}\tPercent: {}".format(algorithm, int(averages[algorithm]), total_cells, percentage))
