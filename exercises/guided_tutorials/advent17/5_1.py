lines = [line.rstrip('\n') for line in open('input.txt')]
instructions = [int(line) for line in lines]
old_index = 0
new_index = 0
steps = 0
while True:
    try:
        new_index += instructions[old_index]
    except IndexError as e:
        break
    instructions[old_index] += 1
    old_index = new_index
    steps += 1
print(steps)


