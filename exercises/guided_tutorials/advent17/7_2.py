from collections import defaultdict


class Node(object):
    def __init__(self, weight, name):
        self.name = name
        self.base_weight = weight
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def get_weight(self):
        weight = self.base_weight
        for child in self.children:
            weight += child.get_weight()
        return weight

    def find_imbalance(self):
        weights = []
        for child in self.children:
            weights.append((child.name, child.get_weight()))
        dict = defaultdict(list)
        for name, weight in weights:
            dict[weight].append(name)
        for weight, name in dict.items():
            if len(name) == 1:
                print('{}: imbalance in {} -- {}'.format(self.name, name[0], weights))
                for child in self.children:
                    if child.name == name[0]:
                        for report_c in child.children:
                            print(report_c.name, report_c.get_weight())
                        child.find_imbalance()


def get_nodes(instruction_list):
    nodes = {}
    for line in instruction_list:
        instruction = line.split('->')
        weight = int(instruction[0].split()[1][1:-1])
        name = instruction[0].split()[0]
        nodes[name] = Node(weight, name)
    return nodes


def get_children(instruction_list, node_list):
    for line in instruction_list:
        instruction = line.split('->')
        if len(instruction) > 1:
            name = instruction[0].split()[0]
            for i in ''.join(instruction[1].split()).split(','):
                node_list[name].add_child(node_list[i])


def main(filename):
    instruction_list = [line.rstrip('\n') for line in open(filename)]
    node_list = get_nodes(instruction_list)
    get_children(instruction_list, node_list)
    node_list['cyrupz'].find_imbalance()

main('input.txt')