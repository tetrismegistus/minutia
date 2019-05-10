from numpy import array, bitwise_xor


def group(iterator, count):
    itr = iter(iterator)
    while True:
        yield array([itr.__next__() for i in range(count)])


def get_instructions(filename):
    with open(filename) as f:
        instructions = [ord(n) for n in f.read().strip('\n')]
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


lengths = get_instructions('input.txt')
sparse_hash = get_sparse_hash(lengths)
dense_hash = [bitwise_xor.reduce(l) for l in group(sparse_hash, 16)]
hex_rep = ''.join(['{:02x}'.format(n) for n in dense_hash])
print(hex_rep)

