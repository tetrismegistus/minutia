def get_structure(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    structure = {}
    for line in lines:
        origin, destination = line.replace(' ', '').split('<->')
        structure[int(origin)] = [int(i) for i in destination.split(',')]
    return structure


def map_relationships(item, item_set):
    for relation in links[item]:
        if relation not in item_set:
            item_set.append(relation)
            map_relationships(relation, item_set)


def count_sets():
    sets = []
    for number in links.keys():
        current_set = []
        map_relationships(number, current_set)
        if set(current_set) not in sets:
            sets.append(set(current_set))
    print(len(sets))

links = get_structure('input.txt')
count_sets()
