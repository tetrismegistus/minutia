import operator

'''
--- Day 2: Bathroom Security ---

You arrive at Easter Bunny Headquarters under cover of 
darkness. However, you left in such a rush that you forgot 
to use the bathroom! Fancy office buildings like this one 
usually have keypad locks on their bathrooms, so you search 
the front desk for the code.

"In order to improve security," the document you find says, 
"bathroom codes will no longer be written down. Instead, 
please memorize and follow the procedure below to access the 
bathrooms."

The document goes on to explain that each button to be 
pressed can be found by starting on the previous button and 
moving to adjacent buttons on the keypad: U moves up, D 
moves down, L moves left, and R moves right. Each line of 
instructions corresponds to one button, starting at the 
previous button (or, for the first line, the "5" button); 
press whatever button you're on at the end of each line. If 
a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out 
the code as you walk to the bathroom. You picture a keypad 
like this:

1 2 3
4 5 6
7 8 9
Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD
You start at "5" and move up (to "2"), left (to "1"), and 
left (you can't, and stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right 
twice (to "3") and then down three times (stopping at "9" 
after two moves and ignoring the third), ending up with 9.
Continuing from "9", you move left, up, right, down, and 
left, ending with 8.
Finally, you move up four times (stopping at "2"), then down 
once, ending with 5.
So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you 
found at the front desk. What is the bathroom code?

Your puzzle answer was 47978.
'''

def map_buttons():
    # buttons are laid in cartesian coordinates with the following button label to coordinate relationships
    # index   0      1      2
    # label   1      2      3
    # coord (0, 0) (1, 0) (2, 0)
    #
    # index   3      4      5
    # label   4      5      6
    # coord (0, 1) (1, 1) (2, 1)
    #
    # index   6      7      8
    # label   7      8      9
    # coord (0, 2) (1, 2) (2, 2)
    buttons = []
    for index in range(1, 4):
        for y_index in range(3):
            button = (y_index, (index - 1) % 3)
            buttons.append(button)
    # this allows me to create a list with those coordinates in order, and because my values are in the
    # this allows me to look up button values by coordinate points because buttons[label - 1] equals the actual button
    # so, for instance, value = buttons.index((2, 1)) + 1 = 6
    return buttons


def evaluate_lines(input_lines, coords, button_map):
    return_list = []
    for input_line in input_lines:
        for char in input_line:
            try:
                test_coords = tuple(map(operator.add, coords, directions.get(char)))
                button_map.index(test_coords)  # if it fails, the direction tried to go off the keypad
                coords = test_coords
            except ValueError:
                pass
        return_list.append(keypad_buttons.index(coords) + 1)
    return return_list


def read_file(filename):
    lines = [line.rstrip('\n') for line in open(filename)]

    return lines


keypad_buttons = map_buttons()
# this of course leads to the following spatial understanding
directions= {'U': (0, -1),
             'D': (0, 1),
             'L': (-1, 0),
             'R': (1, 0)}

current_coords = (1, 1)  # we start at 5 in call cases

lines = read_file('input.txt')
current_coords = evaluate_lines(lines, current_coords, keypad_buttons)
for item in current_coords:
    print(item, end="")
print()




