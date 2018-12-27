import operator

'''
--- Part Two ---

Then, you notice the instructions continue on the back of 
the Recruiting Document. Easter Bunny HQ is actually at the 
first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the 
first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

Your puzzle answer was 110.

'''

def turn(index, leftorright):
    return (index + leftorright) % 4


def walk(direction, blocks, coordinate):
    for block in range(blocks):
        coordinate = tuple(map(operator.add, coordinate, direction))

    return coordinate


def parse_string(input_string):
    direction = input_string[:1]
    if direction == "R":
        direction = 1
    else:
        direction = -1
    steps_to_add = int(input_string[1:])

    return direction, steps_to_add


def work_input(input_string):

    direction_index = 0
    current_coord = (0, 0)
    visited = []
    visited.append(current_coord)
    split_string = input_string.split(', ')

    for string_to_work in split_string:
        right_or_left, steps = parse_string(string_to_work)
        direction_index = turn(direction_index, right_or_left)
        current_direction = DIRECTIONS[direction_index]
        for step in range(steps):
            current_coord = walk(current_direction, 1, current_coord)
            if current_coord in visited:
                return abs(current_coord[0]) + abs(current_coord[1])
            visited.append(current_coord)


NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

print(work_input(input("Enter the string: ")))
