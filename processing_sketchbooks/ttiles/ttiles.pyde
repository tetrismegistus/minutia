import random

xmin = -10
xmax = 10
ymin = -10
ymax = 10
rangex = xmax - xmin
rangey = ymax - ymin
x_key = [0 for i in range(rangex / 2)]
y_key = [0 for i in range(rangey / 2)]
board = [[random.randint(0, 1) for x in x_key] for y in y_key]

name = 0

def block_zero(x, y):
    arc(x, y, xedge, yedge, 0, HALF_PI)
    arc(x + xedge, y + yedge, xedge, yedge, 2 * HALF_PI, 3 * HALF_PI)
    
def block_one(x, y):        
    segment_end = xedge / 3
    y_coord = y + yscl        
    x1 = (segment_end * 2) + x    
    x2 = (segment_end * 3) + x
    
    line(x + xscl, y, x + xscl, y + yedge)
    line(x, y_coord, segment_end + x, y_coord)
    line(x1, y_coord, x2, y_coord)
    
def block_two(x, y):  
    y_coord = y + yscl          
    x_coord = x + xscl
    segment_end = yedge / 3
    y1 = (segment_end * 2) + y    
    y2 = (segment_end * 3) + y
    
    line(x, y_coord, x + xedge, y_coord)    
    line(x_coord, y, x_coord, segment_end + y)
    line(x_coord, y1, x_coord, y2)
    
    
def block_three(x, y):       
    arc(x + xedge, y, xedge, yedge, HALF_PI, 2*HALF_PI)        
    arc(x, y + yedge, xedge, yedge, radians(270), radians(360))

def setup():
    global xscl, yscl, xedge, yedge, tiles
    size(600, 600)
    xscl = width / rangex
    yscl = height / rangey
    xedge = xscl * 2
    yedge = yscl * 2
    tiles = [block_zero,         
             block_three]
        
def draw():    
    global xscl, yscl, x_key, y_key, name
    
    
    background(100, 100, 100)
    for y in range(0, height, yedge):        
        for x in range(0, width, xedge):
            
    
            fill(x % 255, y % 255, 100)
            stroke(200, x % 255, y % 255)
            tiles[board[x / xedge][y / yedge]](x, y)            
    #save("images/{0:04d}.png".format(name))
    ydx = random.randint(0, len(board) - 1)
    xdx = random.randint(0, len(board[0]) - 1)
    
    if board[ydx][xdx] == 0:
        board[ydx][xdx] = 1
    else:
        board[ydx][xdx] = 0
         
    name += 1
    
    
            
