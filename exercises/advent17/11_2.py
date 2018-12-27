from numpy import array


def distance(coord):
    return int((abs(coord[0]) + abs(coord[1]) + abs(coord[2])) / 2)


def ariadne(instruction_list):
    coord = array([0, 0, 0])
    
    compass = {'n':  array([0, 1, -1]),
               'nw': array([-1, 1, 0]),
               'ne': array([1, 0, -1]),
               's':  array([0, -1, 1]),
               'sw': array([-1, 0, 1]),
               'se': array([1, -1, 0])}

    max_distance = 0

    for instruction in instruction_list.split(','):
        coord += compass[instruction]
        max_distance = distance(coord) if distance(coord) > max_distance else max_distance

    return max_distance

with open('input.txt') as f:
    data = f.read().strip('\n')

print(ariadne(data))

