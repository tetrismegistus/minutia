xmin = -.25
xmax = .25

ymin = -1
ymax = -.5

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600, 600)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height
    colorMode(HSB)
    

def draw():
    z = [0.25, 0.75]
    for x in range(width):
        for y in range(height):
            z = [(xmin + x * xscl),
                 (ymin + y * yscl)]
            col = mandelbrot(z, 100)
            if col == 100:
                fill(0)
            else:
                fill(255-15*col, 255, 255)
            rect(x, y, 1, 1)
            
    println(mandelbrot(z, 10))



def mandelbrot(z, num):
    '''runs the process num times
    and returns the diverge count '''
    count = 0
    z1 = z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1=cAdd(cMult(z1, z1), z)
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
    
