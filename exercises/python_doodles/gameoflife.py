#!/usr/bin/env python3

import copy, os, time, csv, random, curses
from curses import wrapper

def debug(stdscr,var):
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()
    import pdb; pdb.set_trace()

def print_matrix(matrix):
    xindex = 0
    for x in matrix:    
        yindex = 0
        for y in x:
            yindex += 1        
            if y == True:
                stdscr.addstr(xindex + 1,yindex, "*", curses.color_pair(2))
            else:
                stdscr.addstr(xindex + 1 ,yindex, " ", curses.color_pair(1))
        xindex += 1

def get_input(prompt, default, x = 0, y = 1, color_pair = 1):
    stdscr.addstr(x,y, prompt, curses.color_pair(1))
    stdscr.refresh()
    curses.echo()
    value = stdscr.getstr(0, len(prompt) + 1)
    curses.noecho()
    stdscr.clear() 
    if value:
        return value
    else:
        return default

def read_file(filename):
    data = list(csv.reader(open(filename, "r")))
    xindex = 0
    yindex = 0
    
    for x in data:        
        yindex = 0 
        for y in x:
            if y.upper() == "FALSE":
                data[xindex][yindex] = False
            else:
                data[xindex][yindex] = True
            yindex += 1
        xindex += 1 
    return data


def populate_field(percent=50):
    return random.randrange(100) < percent 

def tick(matrix):
    xindex = 0
    newmatrix = copy.deepcopy(matrix)
    for x in matrix:
        yindex = 0
        for y in x:
            livecells = 0
            # check each adjacent & diaganol cell for life
            # modular arithmetic used to avoid a dead wall 
            # at the edge conditions and instead bend map
            # into a roughly toroidal shape
            #pdb.set_trace() 
            h = len(matrix) 
            w = len(matrix[0])
            north  = matrix[(xindex - 1) % h][yindex]
            northeast = matrix[(xindex - 1) % h][(yindex + 1) % w]
            east = matrix[xindex][(yindex + 1) % w]
            southeast = matrix[(xindex + 1) % h][(yindex + 1) % w]
            south = matrix[(xindex + 1) % h][yindex]
            southwest = matrix[(xindex + 1) % h][(yindex - 1) % w]
            west = matrix[xindex][(yindex - 1) % w]
            northwest = matrix[(xindex - 1) % h][(yindex - 1) % w]
            
            for x in [north, northeast, east, southeast, south, southwest, west, northwest]:
                if x == True:
                    livecells += 1
                    
            # Any live cell with fewer than two live neighbours dies, as if caused by under-population.
            # Any live cell with two or three live neighbours lives on to the next generation.
            # Any live cell with more than three live neighbours dies, as if by over-population.
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if livecells < 2 and y:
                newmatrix[xindex][yindex] = False
            elif livecells in range(2, 3) and y:
                newmatrix[xindex][yindex] = True
            elif livecells > 3 and y:
                newmatrix[xindex][yindex] = False
            elif livecells == 3:
                newmatrix[xindex][yindex] = True
            
            yindex += 1
        xindex += 1
    return newmatrix

stdscr = curses.initscr()
curses.start_color() 

def main(stdscr):
    
    stdscr.clear()    
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_RED)
    percent = int(get_input(prompt="Fill percentage [enter = 50]: ", default=50))
    
    
    wh = stdscr.getmaxyx()  
    filename="test2.csv"
    matrix = [[populate_field(percent) for x in range(wh[1] - 2)] for y in range(wh[0] - 2)]
    #matrix = list(read_file(filename)) 
    print_matrix(matrix)
    
    while True:           
        cycles = get_input(prompt="Cycles [enter = 1]: ", default=1)
        stdscr.refresh()
        
        # forgive me for the following
        # basically I don't know because I've picked up poor 
        # type habits, which python doesn't discourage,
        # what state my input will be in
        # if it's an integer I can go straight to iteration
        # but if its not, I need to decode it to a string
        # and check if it is reset or exit, to perform those
        # respective functions.  But if it's an int AFTER I've 
        # decoded (perhaps abstract int check to function?) 
        # I can move on to iteration, or start all over 
        # for any other exceptions 

        try: 
            cycles += 0
        except TypeError:
            cycles = cycles.decode('UTF-8')
            if cycles == "reset":
                break
            elif cycles == "exit":
                exit()
            else:
                try:
                    int(cycles)
                    pass
                except ValueError:
                        break

        for x in range(int(cycles)):
            #debug(stdscr, x)
            stdscr.clear()
            print_matrix(matrix)
            stdscr.refresh()
            matrix = tick(matrix)
            time.sleep(.1)
        
        stdscr.clear()
        matrix = tick(matrix)
        print_matrix(matrix)

if __name__ == '__main__':
    while True:
        wrapper(main)
