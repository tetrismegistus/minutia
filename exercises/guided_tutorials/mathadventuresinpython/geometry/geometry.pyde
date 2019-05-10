CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

t = 0

def setup():
    size(600, 600)
    rectMode(CENTER)
    
def draw():
    global t
    background(*BLUE)
    translate(width/2, height/2)
    rotate(radians(t))
    fill(*ORANGE)
    for i in range(12):
        pushMatrix()
        translate(200, 0)
        rotate(radians(5*t))
        rect(0, 0, 576, 18)
        popMatrix()
        rotate(radians(360/12))
    t += .5
    
    
