'''
--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its 
movements, and the clock's oscillator is regulated by stars. 
Unfortunately, the stars have been stolen... by the Easter 
Bunny. To save Christmas, Santa needs you to retrieve all 
fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made 
available on each day in the advent calendar; the second 
puzzle is unlocked when you complete the first. Each puzzle 
grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city 
somewhere. "Near", unfortunately, is as close as you can get 
- the instructions on the Easter Bunny Recruiting Document 
the Elves intercepted start here, and nobody had time to 
work them out further.

The Document indicates that you should start at the given 
coordinates (where you just landed) and face North. Then, 
follow the provided sequence: either turn left (L) or right 
(R) 90 degrees, then walk forward the given number of 
blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on 
foot, though, so you take a moment and work out the 
destination. Given that you can only walk on the street grid 
of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, 
or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting 
position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?

Your puzzle answer was 161.
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

    split_string = input_string.split(', ')

    for string_to_work in split_string:
        right_or_left, steps = parse_string(string_to_work)
        direction_index = turn(direction_index, right_or_left)
        current_direction = DIRECTIONS[direction_index]
        current_coord = walk(current_direction, steps, current_coord)

    print(abs(current_coord[0]) + abs(current_coord[1]))


NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

work_input(input("Enter the string: "))
