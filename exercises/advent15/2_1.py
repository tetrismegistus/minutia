from itertools import combinations
import functools
import operator

lines = [line.rstrip('\n').split('x') for line in open('input.txt')]

total = 0
for package in lines:
    pairs = list(combinations([int(m) for m in package], 2))
    sides = [functools.reduce(operator.mul, pair, 1) for pair in pairs]
    area = 0
    for side in sides:
        area += (2 * side)
    total += area + min(sides)

print(total)



