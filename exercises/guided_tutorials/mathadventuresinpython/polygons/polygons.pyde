def setup():
    size(600, 600)
    
def draw():
    psize = 50
    sides = 3
    for c in range(1, 5):
        for r in range(1, 5):
            pushMatrix()
            translate((psize*c)*2.5, (psize*r)*2.5)            
            polygon(sides, psize)
            popMatrix() 
            sides += 1
         
    
def polygon(sides, sz):
    beginShape()
    for i in range(sides):
        step = radians(360/sides)
        vertex(sz*cos(i*step),
               sz*sin(i*step))
    endShape(CLOSE)
