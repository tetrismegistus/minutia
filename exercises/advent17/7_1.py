def process_file(filename):
    children = []
    parents = []
    lines = [line.rstrip('\n') for line in open(filename)]
    for line in lines:
        instruction = line.split('->')
        parents.append(instruction[0].split()[0])
        if len(instruction) > 1:
            for i in ''.join(instruction[1].split()).split(','):
                children.append(i)
    return set(parents) - set(children)

print(process_file('input.txt'))
