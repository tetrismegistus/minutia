import functools
import operator

lines = [line.rstrip('\n').split('x') for line in open('input.txt')]
total = 0
for package in lines:
    converted = [int(side) for side in package]
    bow = functools.reduce(operator.mul, converted, 1)
    converted.pop(converted.index(max(converted)))
    bowforsides = 0
    for square in [side*2 for side in converted]:
        bowforsides += square
    total += bow + bowforsides

print(total)



