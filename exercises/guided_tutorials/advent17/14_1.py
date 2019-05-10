from numpy import array, bitwise_xor


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


puzzle_input = 'ljoxqyyw'
seq = []
for r in range(128):
    input_string = '{}-{}'.format(puzzle_input, r)
    instructions = get_instructions(input_string)
    sparse_hash = get_sparse_hash(instructions)
    dense_hash = [bitwise_xor.reduce(l) for l in group(sparse_hash, 16)]
    hex_rep = ''.join(['{:02x}'.format(n) for n in dense_hash])
    for i in hex_rep:
        seq.append('{:04b}'.format(int(i, 16)))
seq = ''.join(seq)
print(seq.count('1'))
