import tkinter
from PIL import ImageTk

from common.grids import distance, grid
from common.Animation import Animation
import common.runtimedefs as rundefs


def find_long_path(w=20, h=20, algo=rundefs.DEFAULTALGO, cell_size=10, palette="winter", walls=True, animation=False):
    if animation:
        animation = Animation()

    m = distance.XRayDistanceGrid(w, h, palette=palette, cell_size=cell_size, walls=walls)
    m = algo(m)

    if animation:
        m.animation = animation

    path_start = m.random_cell()
    m.fill_distances(m[path_start.column, path_start.row])

    new_start, new_distance = m.distances.max()
    m.fill_distances(m[new_start.column, new_start.row])

    goal, new_distance = m.distances.max()
    m.distances = m.distances.path_to(goal)
    m.to_img(cell_size=cell_size).save(rundefs.DIRS['output'] + 'long_path.png')
    if animation:
        m.animation.save_gif()
    # display_window(m)



def flood(w=50, h=50, palette="winter", animation=True, png=False, algo=rundefs.DEFAULTALGO, cell_size=10,
          walls=True):
    if animation:
        animation = Animation()

    m = distance.XRayDistanceGrid(w, h, palette=palette, walls=walls, cell_size=cell_size)
    m = algo(m)

    if animation:
        m.animation = animation

    m.fill_distances(m.random_cell())

    if animation:
        m.animation.save_gif()

    if png:
        # display_window(m)
        m.to_img().save(rundefs.DIRS['output'] + 'flood.png')


def carve_and_flood(w=20, h=20, palette="winter", algo=rundefs.DEFAULTALGO):
    animation = Animation()
    m = distance.XRayDistanceGrid(w, h, palette=palette)
    m = algo(m, animation=animation)
    m.animation = animation
    m.fill_distances(m.random_cell())
    m.animation.save_gif()


def maze_without_walls(w=50, h=50, animation=True, png=False, palette="cubehelix", algo=rundefs.DEFAULTALGO,
                       cell_size=3):

    flood(w, h, animation=animation, png=png, palette=palette, algo=algo, cell_size=cell_size, walls=False)


def plain_jane(w=10, h=10, algo=rundefs.DEFAULTALGO, cell_size=10):
    m = grid.Grid(w, h)
    m = algo(m)
    m.to_img(cell_size=cell_size).save(rundefs.DIRS['output'] + 'plainjane.png')
    # display_window(m)


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