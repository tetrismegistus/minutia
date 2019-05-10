#!/usr/bin/env python3

floor = 0
for line in open('input.txt'):
    for i, x in enumerate(line):
        if x == '(':
            floor += 1
        elif x == ')':
            floor -=1
        if floor == -1:
            print(i + 1)
            break

