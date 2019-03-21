from random import choice

from algorithms.mazes.MazeGenerators import MazeGenerator


class AldousBroder(MazeGenerator):
    def __init__(self, grid, start_at=None, animation=None):
        super(AldousBroder, self).__init__(grid, start_at, animation)
        self.run_algorithm(start_at)

    def run_algorithm(self, start_at):
        if start_at is None:
            start_at = self.grid.random_cell()
        cell = start_at
        unvisited = self.grid.size - 1

        while unvisited > 0:
            neighbor = choice(cell.neighbors())
            if len(neighbor.links) == 0:
                cell.link(neighbor, animation=self.animation, grid=self.grid)
                unvisited -= 1
            cell = neighbor
