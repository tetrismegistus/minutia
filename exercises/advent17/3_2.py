from itertools import product


def make_stack(max_address):
    stack = {(0, 0): 1}
    stride = 0
    position = [0, 0]
    operator = -1
    i = 0

    operations = range(-1, 2)
    operators = list(product(operations, operations))

    while True:
        i = (i + 1) % 2

        if i % 2 == 0:
            stride += 1
            operator *= -1

        for step in range(1, stride + 1):
            value = 0
            for o in operators:
                neighbor = (o[0] + position[0], o[1] + position[1])
                value += stack.get(neighbor, 0)
            stack[tuple(position)] = value
            position[i % 2] += 1 * operator
            if value > max_address:
                return value




maxadd = 265149 
print(make_stack(maxadd))
