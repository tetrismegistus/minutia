CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

xmin = -10
xmax = 10
ymin = -10
ymax = 10
rangex = xmax - xmin
rangey = ymax - ymin
    
def setup():
    global xscl, yscl
    size(600, 600)
    xscl = width / rangex
    yscl = -height / rangey
    
def draw():
    global xscl, yscl
    background(255)
    translate(width/2, height/2)
    grid(xscl, yscl)
    graphFunction()
    
def f(x):
    return sin(x)

def graphFunction():
    x = xmin
    while x <= xmax:
        stroke(*RED)
        line(x * xscl, f(x) * yscl, 
             (x + 0.1) * xscl, f(x + 0.1) * yscl)
        x += .1
    
    
def grid(xscl, yscl):
    strokeWeight(1)
    stroke(*CYAN)
    
    for i in range(xmin, xmax + 1):
        line(i * xscl, ymin * yscl, i * xscl, ymax * yscl)
        line(xmin * xscl, i * yscl, xmax * xscl, i * yscl)
        
    stroke(*BLACK)
    line(0, ymin*yscl, 0, ymax*yscl)
    line(xmin*xscl, 0, xmax*xscl, 0)
    
