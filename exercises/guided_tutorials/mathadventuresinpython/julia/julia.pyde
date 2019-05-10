xmin = -2
xmax = 2

ymin = -2
ymax = 2

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600, 600)
    noStroke()
    xscl = width / rangex
    yscl = -height / rangey
    colorMode(HSB)
    

def draw():
    translate(width/2, height/2)
    x = xmin
    while x < xmax:
        y = ymin
        while y < ymax:
            z = [x, y]
            c = [.135, -.06]
            col = julia(z, c, 100)
            if col == 100:
                fill(0)
            else:
                fill(255-col*3, 255, 255)
            rect(x*xscl, y*yscl, 1, 1)
            y += 0.01
        x += 0.01



def julia(z, c, num):
    '''runs the process num times
    and returns the diverge count '''
    count = 0
    z1 = z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1=cAdd(cMult(z1, z1), c)
        count += 1
    return num

def cAdd(a, b):
    """
    Adds Complex(imaginary) Numbers
    """
    return [a[0] + b[0], 
            a[1] + b[1]]

def cMult(u, v):
    """
    Returns the product of two complex numbers
    """
    return [u[0] * v[0] - u[1] * v[1],
            u[1] * v[0] + u[0] * v[1]]

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)
    
