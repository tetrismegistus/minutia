def get_structure(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    structure = {}
    for line in lines:
        origin, destination = line.replace(' ', '').split('<->')
        structure[int(origin)] = [int(i) for i in destination.split(',')]
    return structure


def map_relationships(item):
    for relation in links[item]:
        if relation not in zero_set:
            zero_set.append(relation)
            map_relationships(relation)


links = get_structure('input.txt')
zero_set = []
map_relationships(0)
print(zero_set)
print(len(zero_set))
