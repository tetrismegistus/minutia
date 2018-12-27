#!/usr/bin/env python3

floor = 0
for line in open('input.txt'):
    for x in line:
        if x == '(':
            floor += 1
        elif x == ')':
            floor -=1
        print(floor)

print(floor)
