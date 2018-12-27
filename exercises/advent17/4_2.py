lines = [line.rstrip('\n') for line in open('input.txt')]

valid_count = 0
for line in lines:
    valid = True
    letter_sets = [set(word) for word in line.split()]
    for lset in letter_sets:
        if letter_sets.count(lset) > 1:
            valid = False
            break
    if valid:
        valid_count += 1 

print(valid_count)

