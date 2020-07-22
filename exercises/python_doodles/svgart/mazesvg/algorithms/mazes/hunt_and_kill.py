from random import choice


def hunt_and_kill(grid, animation=None):
    current = grid.random_cell()

    while current:
        unvisited_neighbors = [neighbor for neighbor in current.neighbors() if len(neighbor.links) == 0]

        if len(unvisited_neighbors) > 0:
            neighbor = choice(unvisited_neighbors)
            current.link(neighbor, animation=animation, grid=grid)
            current = neighbor
        else:
            current = None

            for cell in grid.each_cell():
                visited_neighbors = [neighbor for neighbor in cell.neighbors() if len(neighbor.links) > 0]
                if len(cell.links) == 0 and len(visited_neighbors) > 0:
                    current = cell
                    neighbor = choice(visited_neighbors)
                    current.link(neighbor, animation=animation, grid=grid)
                    break


