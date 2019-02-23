from numpy import array

with open('input.txt') as f:
    instructions = [int(n) for n in f.read().strip('\n').split(',')]

orig_list = array(list(range(256)))
index = 0
skip = 0

for instruction in instructions:
    indices = range(index, index+instruction)
    sequence = orig_list.take(indices, mode='wrap')[::-1]
    for i, num in enumerate(sequence):
        orig_list[(i + index) % len(orig_list)] = num
    index = (index + instruction + skip) % len(orig_list)
    skip += 1

print(orig_list[0] * orig_list[1])
