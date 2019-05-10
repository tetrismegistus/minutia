lines = [line.rstrip('\n') for line in open('input.txt')]

total = 0

for string in lines:
    seen = {}
    repetition = False
    palindrome_triplet = False
    for i, char in enumerate(string):
        pair = string[i:i + 2]
        triplet = string[i:i + 3]

        if pair not in seen.keys():
            seen.update({pair: i})
        elif pair in seen.keys() and seen[pair] < i - 1:
            repetition = True

        try:
            if triplet[0] == triplet[2]:
                palindrome_triplet = True
        except:
            break

    if repetition and palindrome_triplet:
        total += 1

print(total)




