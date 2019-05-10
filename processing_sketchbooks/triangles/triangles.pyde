from math import sqrt

T = 0
num_triangles = 90

def setup():
    size(600, 600)
    rectMode(CENTER)
    colorMode(HSB)
    

def draw():
    global T
    global num_triangles
    
    translate(width/2, height/2)
    rotate(radians(T))
    background(0)
    for i in range(num_triangles):
        
        rotate(radians(360/90))
        pushMatrix()
        translate(200, 0)
        rotate(radians(T + 2*i*360/num_triangles))
        h = scaleHue(integer=i, inlow=0, inhigh=90)
        stroke(h, 255, 255)
        tri(100)
        popMatrix()
        
    T += 0.5
    
    
def scaleHue(integer, inlow, inhigh, outlow=0.0, outhigh=255.0):
    integer = float(integer)
    inlow = float(inlow)
    inghigh = float(inhigh)
    return ((integer - inlow) / (inhigh - inlow)) * (outhigh - outlow) + outlow    
    
    
    
def tri(length):
    noFill()
    triangle(0, -length,
             -length * sqrt(3)/2, length / 2,
             length * sqrt(3)/2, length/2)
               
