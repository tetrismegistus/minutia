"""

    --- Day 8: Two-Factor Authentication ---

    You come across a door implementing what you can only assume is an implementation of two-factor authentication after
    a long game of requirements telephone.

    To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a
    code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

    Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how
    it works. Now you just have to work out what the screen would have displayed.

    The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are
    your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three
    somewhat peculiar operations:

    rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
    rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall
    off the right end appear at the left end of the row. rotate column x=A by B shifts all of the pixels in column A
    (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.

    For example, here is a simple sequence on a smaller screen:

    rect 3x2 creates a small rectangle in the top-left corner:

    ###....
    ###....
    .......
    rotate column x=1 by 1 rotates the second column down by one pixel:

    #.#....
    ###....
    .#.....
    rotate row y=0 by 4 rotates the top row right by four pixels:

    ....#.#
    ###....
    .#.....
    rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to
    the top:

    .#..#.#
    #.#....
    .#.....
    As you can see, this display technology is extremely powerful, and will soon dominate the
    tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you,
    anyway.

    There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen
    did work, how many pixels should be lit?

    Your puzzle answer was 119.

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

total = 0
for row in display:
    for col in row:
        total += col

print(total)
