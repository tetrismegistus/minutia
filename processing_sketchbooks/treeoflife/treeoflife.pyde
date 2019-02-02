from itertools import tee, izip
from collections import namedtuple

SWIDTH = 400
SHEIGHT = 768
TCENTER = SWIDTH / 2       # center of the tree
TIF = 400                  # Tiphereth
KET = 200                  # Kether
BRAD = (TIF - KET)/2       # backbone radius
SRAD = 50                  # sephira radius
BACKBONE = [(TCENTER, c, BRAD) for c in range(KET, KET+BRAD*4, BRAD)]

Sephira = namedtuple('Sephira', ['value', 'x', 'y', 'radius'])
Path = namedtuple('Path', ['x1','y1', 'x2', 'y2'])

def setup():
    size(SWIDTH, SHEIGHT)
    textSize(12)

def draw():
    mercy = []
    severity = []
    balance = []
    paths = []
    
    #draw_backbone()
    
    ycords = [p for p in range(KET, KET+BRAD*5, BRAD)]
    svalues = ['1', 'D', '6', '9', '10']    
    for c, v in zip(ycords, svalues):
        balance.append(Sephira(v, TCENTER, c, SRAD))
        
    svalues = ['2', '3', '4', '5', '7', '8']
    for c1, c2 in pairwise(BACKBONE):    
        for pt in circle_intersection(c1, c2):
            svalue = svalues.pop(0)
            if svalue in '2 4 7'.split():
                mercy.append(Sephira(svalue, pt[0], pt[1], SRAD))
            else:
                severity.append(Sephira(svalue, pt[0], pt[1], SRAD))
                
    for p in [balance, mercy, severity]:
        paths.append(Path(p[0].x, p[0].y, p[-1].x, p[-1].y))
    
    tpoints = balance[:-1]
    for s1, s2 in zip(mercy, severity):    
        tp = tpoints.pop(0)
        bp = tpoints[0] 
        paths.append(Path(tp.x, tp.y, s2.x, s2.y))
        paths.append(Path(tp.x, tp.y, s1.x, s1.y))
        paths.append(Path(s1.x, s1.y, s2.x, s2.y))
        paths.append(Path(bp.x, bp.y, s2.x, s2.y))
        paths.append(Path(bp.x, bp.y, s1.x, s1.y))
        
    binah = severity[0]
    chokmah = mercy[0]
    tiph =  balance[2]
    
    paths.append(Path(severity[0].x, severity[0].y, tiph.x, tiph.y))
    paths.append(Path(mercy[0].x, chokmah.y, tiph.x, tiph.y))
                 
        
    for p in paths:
        line(p.x1, p.y1, p.x2, p.y2)
                    
    for s in balance +  mercy + severity:    
        if s.value == 'D':
            noFill()
        else:
            fill(153)
        #noFill()
        circle(s.x, s.y, s.radius)
        
        if s.value != 'D':
            fill(255, 0, 0)
            text(s.value, s.x-textWidth(s.value)/2, s.y+4)
        
def circle(x, y, rad):
    ellipse(x, y, rad, rad)

def draw_backbone():
    noFill()
    [circle(c[0], c[1], c[2]*2) for c in BACKBONE]

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a,b)    
    
def circle_intersection(circle1, circle2):
    # https://gist.github.com/xaedes/974535e71009fa8f090e
    # thanks!
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    dx,dy = x2-x1,y2-y1
    d = dist(x1, y1, x2, y2)
    
    if d > r1 + r2:
        return None # circles are separate
    elif d < abs(r1 - r2):
        return None # circle within another
    elif d == 0 and r1 == r2:
        return None # circles are coincident
    
    a = (r1*r1-r2*r2+d*d)/(2*d)
    h = sqrt(r1*r1-a*a)
    xm = x1 + a*dx/d
    ym = y1 + a*dy/d
    xs1 = xm + h*dy/d
    xs2 = xm - h*dy/d
    ys1 = ym - h*dx/d
    ys2 = ym + h*dx/d

    return (xs1,ys1),(xs2,ys2)
