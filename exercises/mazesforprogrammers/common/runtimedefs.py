from algorithms.mazes.hunt_and_kill import hunt_and_kill
from algorithms.mazes.recursive_backtracker import TrueRecursiveBacktracker
from algorithms.mazes.wilsons import wilsons
from algorithms.mazes.sidewinder import sidewinder
from algorithms.mazes.aldous_broder import AldousBroder

DIRS = {'output': 'output/'}
DIRS['staging'] = DIRS['output'] + 'staging/'

DEFAULTALGO = TrueRecursiveBacktracker
DEFAULTW = 20
DEFAULTH = 20

STATE_LOOKUP = {'#00ffff': [TrueRecursiveBacktracker, "Purples", False],
                '#0000ff': [TrueRecursiveBacktracker, "GnBu_d", True],
                '#ffffff': [TrueRecursiveBacktracker, "Reds", True],
                '#ff0000': [TrueRecursiveBacktracker, "GnBu_d", True],
                '#ff00ff': [TrueRecursiveBacktracker, "hls", True],
                '#ffff00': [TrueRecursiveBacktracker, "GnBu_d", True],
                '#00ff00': [TrueRecursiveBacktracker, "Oranges", True]}
