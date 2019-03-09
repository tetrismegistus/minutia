from random import choice


def aldous_broder(grid, animation=None):
    cell = grid.random_cell()
    unvisited = grid.size - 1

    while unvisited > 0:
        neighbor = choice(cell.neighbors())
        if len(neighbor.links) == 0:
            cell.link(neighbor, animation=animation, grid=grid)
            unvisited -= 1
        cell = neighbor

