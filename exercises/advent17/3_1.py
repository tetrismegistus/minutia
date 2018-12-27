def make_stack(max_address):
    stack = {}
    stride = 0
    position = [0, 0]
    operator = -1
    address = 1
    i = 0
    while address < max_address:
        i = (i + 1) % 2

        if i % 2 == 0:
            stride += 1
            operator *= -1

        for step in range(1, stride + 1):
            stack[address] = position[:]
            position[i % 2] += 1 * operator
            address += 1
            if address > max_address:
                break

    return stack


def manhattan_distance(destination):
    return(abs(destination[0]) + abs(destination[1]))

maxadd = 265149
stack = make_stack(maxadd)
print(manhattan_distance(stack[maxadd]))
