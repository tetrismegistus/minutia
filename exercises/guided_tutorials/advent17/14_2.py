from numpy import array, bitwise_xor
from collections import defaultdict


class Disk:
    operators = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def __init__(self, data):
        self.data = data
        self.regions = defaultdict(list)
        self.define_regions()

    def fill_region(self, xytuple, target):
        try:
            if self.data[xytuple[0]][xytuple[1]] == 1:
                if xytuple not in self.regions[target]:
                    self.regions[target].append(xytuple)
                    for operation in Disk.operators:
                        x = xytuple[0] + operation[0]
                        y = xytuple[1] + operation[1]
                        if x >= 0 and y >= 0:
                            self.fill_region((x, y), target)
            return
        except:
            return

    def in_regions(self, xytuple):
        for region in self.regions:
            if xytuple in self.regions[region]:
                return True
        return False

    def define_regions(self):
        current_region = 0
        for r, row in enumerate(self.data):
            for c, column in enumerate(row):
                if column == 1 and not self.in_regions((r, c)):
                    self.fill_region((r, c), current_region)
                    current_region += 1


def group(iterator, count):
    itr = iter(iterator)
    while True:
        yield array([itr.__next__() for i in range(count)])


def get_instructions(string):
    instructions = [ord(n) for n in string]
    instructions += [17, 31, 73, 47, 23]
    return instructions


def get_sparse_hash(length_list):
    orig_list = array(list(range(256)))
    index = 0
    skip = 0
    for r in range(64):
        for length in length_list:
            indices = range(index, index + length)
            sequence = orig_list.take(indices, mode='wrap')[::-1]
            for i, num in enumerate(sequence):
                orig_list[(i + index) % len(orig_list)] = num
            index = (index + length + skip) % len(orig_list)
            skip += 1
    return orig_list


def fill_disk(puzzle_input):
    data = []
    for r in range(128):
        row = []
        input_string = '{}-{}'.format(puzzle_input, r)
        instructions = get_instructions(input_string)
        sparse_hash = get_sparse_hash(instructions)
        dense_hash = [bitwise_xor.reduce(l) for l in group(sparse_hash, 16)]
        hex_rep = ''.join(['{:02x}'.format(n) for n in dense_hash])
        for i in hex_rep:
            bin_string = '{:04b}'.format(int(i, 16))
            for b in bin_string:
                row.append(int(b))
        data.append(row)
    return data


disk_data = fill_disk('ljoxqyyw')
disk = Disk(disk_data)
print(max(disk.regions.keys()) + 1)
