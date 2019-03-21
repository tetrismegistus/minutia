from abc import abstractmethod


class MazeGenerator:
    def __init__(self, grid, start_at, animation=None):
        self.animation = animation
        self.grid = grid

    @abstractmethod
    def run_algorithm(self, start_at):
        pass
