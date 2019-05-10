# this is readable, right?
sheet = [[int(num) for num in row] for row in [line.rstrip('\n').split('\t') for line in open('input.txt')]]
differences = []
for row in sheet:
    differences.append(max(row) - min(row))

print(sum(differences))