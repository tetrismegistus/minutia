import svgwrite
import math


class JupiterSeal:
    def __init__(self, width=200, height=200, smallr=2, edge_dist=5, filename='jupseal.svg'):
        self.width = width
        self.height = height
        self.filename = filename
        self.smallr = smallr
        self.drawing = svgwrite.Drawing(filename, profile='full', size=(width, height))
        self.edge_dist = edge_dist
        self.drawing.stroke('black')
        self.drawing.fill('none')
        cir1 = (self.edge_dist, self.edge_dist)
        cir2 = (self.width - self.edge_dist, self.height - self.edge_dist)
        cir3 = (self.width - self.edge_dist, self.edge_dist)
        cir4 = (self.edge_dist, self.height - self.edge_dist)
        self.connected_circles(cir1, cir2, 45, 225)
        self.connected_circles(cir3, cir4, 135, 315)
        self.drawing.add(self.drawing.add(self.drawing.rect(insert=(0, 0), size=(self.width, self.height))))
        self.drawing.add(self.drawing.circle(center=(width/2, height/2), r=((width - self.edge_dist) / 2) - 1))
        self.drawing.save(filename)

    def connected_circles(self, cir1, cir2, cir1ang, cir2ang):
        self.drawing.add(self.drawing.circle(center=cir1, r=self.smallr))
        startx = cir1[0] + self.smallr * math.cos(math.radians(cir1ang))
        starty = cir1[1] + self.smallr * math.sin(math.radians(cir1ang))
        self.drawing.add(self.drawing.circle(center=cir2, r=self.smallr))
        endx = cir2[0] + self.smallr * math.cos(math.radians(cir2ang))
        endy = cir2[1] + self.smallr * math.sin(math.radians(cir2ang))
        self.drawing.add(self.drawing.line((startx, starty), (endx, endy)))



JupiterSeal()