def get_repeating_digits(sequence):
    repeating_sum = 0
    step = int(len(sequence) / 2)
    for index, digit in enumerate(sequence):
        if sequence[(index + step) % len(sequence)] == digit:
            repeating_sum += digit
    return repeating_sum

lines = [line.rstrip('\n') for line in open('input.txt')]
for line in lines:
    digits = [int(d) for d in line]
    print(get_repeating_digits(digits))
