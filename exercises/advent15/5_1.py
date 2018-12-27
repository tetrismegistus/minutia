lines = [line.rstrip('\n') for line in open('input.txt')]

total = 0


for string_list in lines:
    vowels = 0
    repetition = False
    curse_words = False

    for i, string in enumerate(string_list):

        if string in 'aeiou':
            vowels += 1

        try:
            if string == string_list[i+1]:
                repetition = True
        except:
            break

        if string_list[i:i+2] in ['ab', 'cd', 'pq', 'xy']:
            curse_words = True
            break

    if ((vowels >= 3) and repetition) and not curse_words:
        total += 1

print(total)
