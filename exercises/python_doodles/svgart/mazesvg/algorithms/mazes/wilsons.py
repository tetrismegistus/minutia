from random import choice


def wilsons(grid, animation=None):
    unvisited = [c for c in grid.each_cell()]
    first = choice(unvisited)
    unvisited.remove(first)

    while len(unvisited) > 0:
        cell = choice(unvisited)
        path = [cell]
        while cell in unvisited:
            cell = choice(cell.neighbors())
            if cell in path:
                position = path.index(cell)
                path = path[:position + 1]
            else:
                path.append(cell)

        for i in range(len(path) - 1):
            path[i].link(path[i + 1], animation=animation, grid=grid)
            unvisited.remove(path[i])

    return grid
