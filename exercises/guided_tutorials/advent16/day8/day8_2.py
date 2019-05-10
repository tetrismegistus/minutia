"""
    --- Part Two ---

    You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5
    pixels wide and 6 tall.

    After you swipe your card, what code is the screen trying to display?

    Your puzzle answer was ZFHFSFOGPO.

    Both parts of this puzzle are complete! They provide two gold stars: **
"""

def parse_line(user_input):
    user_input = user_input.split()
    token = user_input.pop(0)
    if token.lower() == 'rect':
        user_input = ''.join(user_input)
        user_input = user_input.split('x')
        rect(int(user_input[0]), int(user_input[1]), display)
    elif token.lower() == 'rotate':
        command_type = user_input.pop(0)
        token1 = int(user_input[0][2:])
        token2 = int(user_input[2])
        rotate(command_type, token1, token2)


def show_screen(screen_array):
    for row in screen_array:
        for column in row:
            if column:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()


def rect(x, y, screen_array):
    for row in range(len(screen_array)):
        for column in range(len(screen_array[0])):
            if row < y and column < x:
                screen_array[row][column] = 1


def rotate(command_string, position, rotation):
    if command_string == 'row':
        copy = display[position][:]
        for item in range(len(copy)):
            copy[item] = display[position][(item - rotation)]
        display[position] = copy[:]
    elif command_string == 'column':
        reference = []
        for row in range(len(display)):
            for col in range(len(display[row])):
                if col == position:
                    reference.append(display[row][col])

        copy = reference[:]
        for item in range(len(copy)):
            copy[item] = reference[item - rotation]

        for row in range(len(display)):
            for col in range(len(display[row])):
                if col == position:
                    display[row][col] = copy[row]


display = [[0 for x in range(50)] for y in range(6)]

file_name = 'input.txt'
file_lines = [line.rstrip('\n') for line in open(file_name)]
count = 0
for line in file_lines:
    parse_line(line)

show_screen(display)
