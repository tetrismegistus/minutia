lines = [line.rstrip('\n') for line in open('input.txt')]

valid_count = 0
for line in lines:
    if len(line.split()) == len(set(line.split())):
            valid_count += 1

print(valid_count)

