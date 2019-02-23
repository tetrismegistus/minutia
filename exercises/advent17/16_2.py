def load_steps(filename):
    with open(filename) as f:
        file = f.read().strip('\n').split(',')

    steps = []

    for instruction in file:
        step = [instruction[0]] + instruction[1:].split('/')
        steps.append(step)

    return steps


def spin(string, number):
    index = -(number % len(string))
    return string[index:] + string[:index]


def index_swap(string, index1, index2):
    target_string = list(string)
    s1, s2 = string[index1], string[index2]
    target_string[index1] = s2
    target_string[index2] = s1
    return ''.join(target_string)


def partner_swap(string, letter1, letter2):
    index1 = string.index(letter1)
    index2 = string.index(letter2)
    return index_swap(string, index1, index2)


def dance(steps, line):
    for step in steps:
        if step[0] == 's':
            line = spin(line, int(step[1]))
        elif step[0] == 'x':
            line = index_swap(line, int(step[1]), int(step[2]))
        elif step[0] == 'p':
            line = partner_swap(line, step[1], step[2])
    return line


def main(filename):
    steps = load_steps(filename)
    line = ''.join([chr(i) for i in range(97, 113)])
    reference = line
    iterations = 0
    while True:
        iterations += 1
        line = dance(steps, line)
        if line == reference:
            break
    for s in range(1000000000 % iterations):
        line = dance(steps, line)
    print(line)


main('input.txt')




