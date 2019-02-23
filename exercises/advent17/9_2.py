with open('input.txt') as f:
    data = f.read()

index = 0
garbage = False
score = 0
scores = [0]
garbage_chars = 0

while True:
    if index > len(data) - 1:
        break
    char = data[index]
    if garbage:
        if char == '!':
            index += 1
        elif char == '>':
            garbage = False
        else:
            garbage_chars += 1
    elif char == '<':
        garbage = True
    elif char == '{':
        scores.append(scores[-1] + 1)
        score += scores[-1]
    elif char == '}':
        scores.pop()
    index += 1

print(garbage_chars)


