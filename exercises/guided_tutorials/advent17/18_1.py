from collections import defaultdict


def decode(value):
    try:
        result = int(value)
    except ValueError:
        result = registers[value]
    return result


def read_file(filename):
    with open(filename) as f:
        instructions = f.read().strip('\n').splitlines()
    instructions = [i.split() for i in instructions]
    return instructions

registers = defaultdict(int)
operations = read_file('input.txt')
last_frequency = 0

index = 0
while True:
    operation = operations[index]

    try:
        target1 = decode(operation[1])
        target2 = decode(operation[2])
    except IndexError:
        pass

    if operation[0] == 'set':
        print('Setting {} to {}'.format(operation[1], target2))
        registers[operation[1]] = target2
    elif operation[0] == 'add':
        registers[operation[1]] += target2
        print('Adding {} to {}'.format(target2, operation[1]))
    elif operation[0] == 'mul':
        registers[operation[1]] *= target2
        print('Multiplying {} by {}'.format(operation[1], target2))
    elif operation[0] == 'mod':
        registers[operation[1]] %= target2
        print('Setting {} to modulus {}'.format(operation[1], target2))
    elif operation[0] == 'snd':
        print('Playing frequency {}'.format(target1))
        last_frequency = target1
    elif operation[0] == 'rcv':
        if target1 != 0:
            print('Last received sound was {}'.format(last_frequency))

    if operation[0] == 'jgz':
        if target1 > 0:
            index += target2
        else:
            index += 1
    else:
        index += 1

print(registers)

