from random import choice

from algorithms.mazes.MazeGenerators import MazeGenerator


class StackRecursiveBacktracker(MazeGenerator):
    def __init__(self, grid, start_at=None, animation=None):
        super(StackRecursiveBacktracker, self).__init__(grid, start_at, animation)
        if not start_at:
            start_at = grid.random_cell()
        self.run_algorithm(start_at)

    def run_algorithm(self, start_at):
        stack = [start_at]

        while len(stack) > 0:
            current = stack[-1]
            neighbors = [n for n in current.neighbors() if len(n.links) == 0]

            if len(neighbors) == 0:
                stack.pop()
            else:
                neighbor = choice(neighbors)
                current.link(neighbor, animation=self.animation, grid=self.grid)
                stack.append(neighbor)


class TrueRecursiveBacktracker(MazeGenerator):
    def __init__(self, grid, start_at=None, animation=None):
        super(TrueRecursiveBacktracker, self).__init__(grid, start_at, animation)
        if not start_at:
            start_at = grid.random_cell()
        self.run_algorithm(start_at)

    def run_algorithm(self, start_at):
        while True:
            neighbors = [n for n in start_at.neighbors() if len(n.links) == 0]

            if len(neighbors) == 0:
                return

            neighbor = choice(neighbors)
            start_at.link(neighbor, animation=self.animation, grid=self.grid)
            self.run_algorithm(neighbor)

