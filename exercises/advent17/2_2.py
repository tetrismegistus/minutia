from itertools import combinations
# this is readable, right?
sheet = [[int(num) for num in row] for row in [line.rstrip('\n').split('\t') for line in open('input.txt')]]


quotients = []
for row in sheet:
    pairs = list(combinations(row, 2))
    for pair in pairs:
        if pair[0] % pair[1] == 0:
            quotients.append(pair[0] / pair[1])
        elif pair[1] % pair[0] == 0:
            quotients.append(pair[1] / pair[0])

print(sum(quotients))