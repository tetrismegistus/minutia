from math import sin, pi
from random import gauss
import svgwrite


def calcWave(dx, ypoints, theta=0, amplitude=500):
    theta += 0.02
    x = theta
    for i in range(len(ypoints)):
        ypoints[i] = sin(x) * amplitude
        x += dx
    return ypoints


def renderwavegauss(ypoints, width=1024, height=768, filename='sinewave.svg', xspacing=16, stderr=1):
    drawing = svgwrite.Drawing(filename, profile='full', size=(width, height))
    drawing.fill('none')
    drawing.stroke('black')
    points = []
    for yidx, yvalue in enumerate(ypoints):
        points.append((int(gauss(yidx * xspacing, stderr)), int(gauss(height/2 + yvalue, stderr))))

    drawing.add(drawing.polyline(points))
    drawing.save(filename)


def renderwave(ypoints, width=1024, height=768, filename='sinewave.svg', xspacing=16):
    drawing = svgwrite.Drawing(filename, profile='full', size=(width, height))
    drawing.fill('none')
    drawing.stroke('black')
    points = []
    for yidx, yvalue in enumerate(ypoints):
        points.append((yidx * xspacing, height/2 + yvalue))

    drawing.add(drawing.polyline(points))
    drawing.save(filename)


width = 1024
wavewidth = width
period = 1000                        # how many pixels before wave repeats
xspacing = 10                       # how far apart for horizontal spacing of points
ypoints = [wavewidth / xspacing]    # height values for the wave
dx = ((2 * pi) / period) * xspacing

for x in range(200, 1, -1):
    ypoints.append(x / xspacing)
    calcWave(dx, ypoints)

renderwavegauss(ypoints, filename='1.svg')
renderwavegauss(ypoints, filename='3.svg', stderr=3)
renderwave(ypoints, filename='0.svg')






