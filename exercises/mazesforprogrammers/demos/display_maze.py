import tkinter
from PIL import ImageTk


def all_distances_by_point(distance_grid, x, y):
    start = distance_grid[x, y]
    distance_grid.distances = start.distances()
    return distance_grid


def find_long_path(distance_grid):
    path_start = distance_grid.random_cell()
    distance_grid.fill_distances(distance_grid[path_start.column, path_start.row])
    new_start, new_distance = distance_grid.distances.max()
    distance_grid.fill_distances(distance_grid[new_start.column, new_start.row])
    goal, new_distance = distance_grid.distances.max()
    distance_grid.distances = distance_grid.distances.path_to(goal)
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