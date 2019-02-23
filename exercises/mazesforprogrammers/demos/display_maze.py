import tkinter
from PIL import Image, ImageTk

from common import runtimedefs
from common.grids import grid, distance


def make_maze(w: int, h: int, alg):
    """
    args w: width, integer
         h: height, integer
         alg: algorithm function or method from algorithms.mazes
    """
    g = grid.Grid(w, h)
    alg(g)
    return g


def make_distance_maze(w: int, h: int, alg):
    g = distance.DistanceGrid(w, h)
    alg(g)
    return g


def find_random_path(distance_grid):
    path_start = distance_grid.random_cell()
    path_end = distance_grid.random_cell()
    while path_end == path_start:
        path_end = distance_grid.random_cell()

    distance_grid.distances = path_start.distances()
    distance_grid.distances = distance_grid.distances.path_to(path_end)
    return distance_grid


def all_distances_by_point(distance_grid, x, y):
    start = distance_grid[x, y]
    distance_grid.distances = start.distances()
    return distance_grid


def find_long_path(distance_grid):
    path_start = distance_grid.random_cell()
    distances = path_start.distances()
    new_start, new_distance = distances.max()
    new_distances = new_start.distances()
    goal, new_distance = new_distances.max()
    distance_grid.distances = new_distances.path_to(goal)
    return distance_grid


def display_window(g):
    """
    :param g: grid object
    :return:
    """
    root = tkinter.Tk()
    img = g.to_img()
    tkimage = ImageTk.PhotoImage(img)
    tkinter.Label(root, image=tkimage).pack()
    root.mainloop()


def main(alg=runtimedefs.DEFAULTALGO,
         w=runtimedefs.DEFAULTW,
         h=runtimedefs.DEFAULTW,
         filename=runtimedefs.DIRS['output'] + 'maze.png'):

    maze = make_distance_maze(w, h, alg)
    return all_distances_by_point(maze, 0, 0)

    # maze = find_long_path(maze)
    # print(maze)
    # maze.to_img().save(filename)


if __name__ == '__main__':
    main()
