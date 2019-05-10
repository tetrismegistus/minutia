import pdb
import operator
from itertools import chain

'''
--- Part Two ---

You finally arrive at the bathroom (it's a several minute 
walk from the lobby so visitors can behold the many fancy 
conference rooms and water coolers on this floor) and go 
to punch in the code. Much to your bladder's dismay, the 
keypad is not at all like you imagined it. Instead, you 
are confronted with the result of hundreds of man-hours of 
bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D
You still start at "5" and stop when you're at an edge, but 
given the same instructions as above, the outcome is very 
different:

You start at "5" and don't move at all (up and left are 
both edges), ending at 5.
Continuing from "5", you move right twice and down three 
times (through "6", "7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", 
"C", "C", "B"), ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is 
the correct bathroom code?

Your puzzle answer was 659AD.
'''

class Button(object):
    def __init__(self, coordinate, value):
        self.coord = coordinate
        self.number = value

    def neighbor_check(self, matrix, operation):
        
        directions = {'U': (-1, 0),
                      'D': (1, 0),
                      'L': (0, -1),
                      'R': (0, 1)}
        test_coords = tuple(map(operator.add, self.coord, directions.get(operation)))
        
        for value in test_coords:
            if value < 0 or value > 4:
                return False
        
        test_neighbor = matrix[test_coords[0]][test_coords[1]].number
        
        try:
            if int(test_neighbor):
                return matrix[test_coords[0]][test_coords[1]]
            else:
                return False
        except ValueError:
            return matrix[test_coords[0]][test_coords[1]]
                

class Map(object):
    def __init__(self, filename='input.txt'):
        self.buttons = [['0', '0', '1', '0', '0'],
                        ['0', '2', '3', '4', '0'],
                        ['5', '6', '7', '8', '9'],
                        ['0', 'A', 'B', 'C', '0'],
                        ['0', '0', 'D', '0', '0']]
        self.populate_map()
        self.position = self.buttons[2][0]
        self.filename = filename
        self.thread = [line.rstrip('\n') for line in open(filename)]
        self.follow_thread() 

    def populate_map(self):
        for row, x in zip(self.buttons, range(5)):
            for cell, y in zip(row, range(5)):
                self.buttons[x][y] = Button((x, y), cell)

    def follow_thread(self):
        output = []
        for line in self.thread:
            for char in line:
                test_position = self.position.neighbor_check(self.buttons, char)
                if test_position:
                    #self.position = self.button.cord
                    self.position = test_position
            output.append(self.position.number)
        
        for item in output:
            print(item, end="")
        print()

Map()
