from random import choice


def aldous_wilson(grid, animation=None):
    cell = grid[0, 0]
    unvisited = [c for c in grid.each_cell()]

    while len(unvisited) > grid.size / 2:
        neighbor = choice(cell.neighbors())
        if len(neighbor.links) == 0:
            cell.link(neighbor, animation=animation, grid=grid)
            unvisited.remove(neighbor)
        cell = neighbor

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


def binary_aldous(grid):
    unvisited = [c for c in grid.each_cell()]
    for cell in grid.each_cell():
        if cell.row < grid.rows / 2:
            neighbors = []
            for d in [cell.east, cell.north]:
                if d:
                    neighbors.append(d)
            if len(neighbors) > 0:
                neighbor = choice(neighbors)
                cell.link(neighbor)
            if cell in unvisited:
                unvisited.remove(cell)

            if cell.row == int(grid.rows / 2) and cell.column == int(grid.columns / 2):
                cell.link(cell.south)

    unvisited.remove(cell)

    while len(unvisited) > 0:
        neighbor = choice(cell.neighbors())
        if len(neighbor.links) == 0:
            cell.link(neighbor)
            unvisited.remove(neighbor)
        cell = neighbor

    return grid


