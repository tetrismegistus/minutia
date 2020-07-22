from random import choice


def binary_tree(grid, animation=None):
    for cell in grid.each_cell():
        neighbors = []

        for d in [cell.east, cell.north]:
            if d:
                neighbors.append(d)

        if len(neighbors) > 0:
            cell.link(choice(neighbors), animation=animation, grid=grid)

