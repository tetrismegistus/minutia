from algorithms.mazes.hunt_and_kill import hunt_and_kill
from algorithms.mazes.recursive_backtracker import TrueRecursiveBacktracker
from algorithms.mazes.wilsons import  wilsons
from algorithms.mazes.sidewinder import sidewinder
from algorithms.mazes.aldous_broder import AldousBroder

DIRS = {'output': 'output/'}
DIRS['staging'] = DIRS['output'] + 'staging/'

DEFAULTALGO = sidewinder
DEFAULTW = 20
DEFAULTH = 20
