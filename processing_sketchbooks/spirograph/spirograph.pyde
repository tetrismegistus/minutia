r1 = 300.0  # big circle
r2 = 205.0  #  circle 2
r3 = 5.0    # drawing dot
prop = 0.8

# big circle
x1 = 0
y1 = 0

t = 0 # time
points = []

def setup():
    size(600, 600)
    colorMode(HSB)
    
def draw():
    global r1, r2, x1, y1, t, prop, points

    
    translate(width/2, height/2)
    background(0)
    noFill()
    
    # big circle
    stroke(0)
    # ellipse(x1, y1, 2*r1, 2*r1)
    
    # small circle
    x2 = (r1 - r2) * cos(t)
    y2 = (r1 - r2) * sin(t)
    # ellipse(x2, y2, 2*r2, 2*r2)

    # drawing dot
    x3 = x2 + prop * (r2 - r3) * cos(-((r1 - r2) / r2) * t)
    y3 = y2 + prop * (r2 - r3) * sin(-((r1 - r2) / r2) * t)
    fill(120, 255, 255)
    # ellipse(x3, y3, 2 * r3, 2 * r3)
    
    line_length = 5500
    points = [[x3, y3]] + points[:line_length]
    for i, p in enumerate(points):
        if i < len(points) - 1:
            stroke(scaleHue(i, 0, line_length), 255, 255)
            line(p[0],p[1],points[i+1][0],points[i+1][1])
    
    t += 0.05
    
    
def scaleHue(integer, inlow, inhigh, outlow=0.0, outhigh=255.0):
    integer = float(integer)
    inlow = float(inlow)
    inghigh = float(inhigh)
    return ((integer - inlow) / (inhigh - inlow)) * (outhigh - outlow) + outlow  

    
