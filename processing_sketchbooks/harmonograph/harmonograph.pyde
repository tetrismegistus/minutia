def setup():
    size(600, 600)
    colorMode(HSB)
    
def draw():    
    background(255)
    translate(width/2, height/2)
    
    points = []
    t = 0
    while t < 1000:
        points.append(harmonograph(t))
        t += 0.01

    for i, p in enumerate(points):
        stroke(scaleHue(i, 0, len(points)), 255, 255)
        
        if i < len(points) - 1:
            line(p[0], p[1], points[i + 1][0], points[i + 1][1])
                    
    
def harmonograph(t):
    a1=a2=a3=a4 = 100
    f1,f2,f3,f4 = 2.01, 3, 3, 2
    p1, p2, p3, p4 = -PI/4, 0, PI/16, 0
    d1, d2, d3, d4 = 0.0003, 0.5, 0, 0
    x = a1 * cos(f1 * t + p1) * exp(-d1 * t) + a3*cos(f3*t + p3)*exp(-d3*t)
    y = a2 * cos(f2 * t + p2) * exp(-d2 * t) + a4*cos(f4*t + p4)*exp(-d4*t)
    return [x, y]


def scaleHue(integer, inlow, inhigh, outlow=0.0, outhigh=255.0):
    integer = float(integer)
    inlow = float(inlow)
    inghigh = float(inhigh)
    return ((integer - inlow) / (inhigh - inlow)) * (outhigh - outlow) + outlow  
