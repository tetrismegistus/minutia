from random import choice

d = 0
spotx = 0
spoty = 0

def setup():
    size(600, 600)
    rectMode(CENTER)
    colorMode(HSB)
    
def draw():
    global d
    global spotx
    global spoty
    
    background(0)
    translate(20, 20)
    movements = [-10, 0, 10]
    spotx = limit(spotx + choice(movements), maximum=600)
    spoty = limit(spoty + choice(movements), maximum=600)
    
    for x in range(20):
        for y in range(20):
            d = dist(30*x, 30*y, mouseX, mouseY)
            fill(0.5*d, 255, 255)
            rect(30*x, 30*y, 25, 25)

def limit(num, minimum=0, maximum=255):
    return max(min(num, maximum), minimum)
