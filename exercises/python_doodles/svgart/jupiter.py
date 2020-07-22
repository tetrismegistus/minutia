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


class JupiterSign:
    def __init__(self, width=200, height=200, edge_dist=5, filename='jupign.svg'):
        self.width = width
        self.height = height
        self.filename = filename
        self.drawing = svgwrite.Drawing(filename, profile='full', size=(width, height))
        self.edge_dist = edge_dist
        self.drawing.stroke('black')
        self.drawing.fill('none')
        lines = [[(self.width/2, self.height/4),
                  (self.width/2, self.height - self.height/4)],
                 [(self.width / 4, self.height/2),
                  (self.width - self.width/4, self.height/2)],
                 [(self.width/2 - edge_dist, self.height/4),
                  (self.width - self.width/2 + edge_dist, self.height/4)],
                 [(self.width/2 - edge_dist, self.height - self.height/4),
                  (self.width - self.width/2 + edge_dist, self.height - self.height/4)],
                 [(self.width - self.width/4, self.height/2 - edge_dist),
                  (self.width - self.width/4, self.height/2 + edge_dist)]]

        for line in lines:
            self.drawing.add(self.drawing.line(line[0], line[1]))
        r = ((self.width - self.width/5) - self.width/4)/3.75
        arc_center = (width/4, height/2 - r)
        arc_points = []
        for degree in range(270, 450):
            arcx = arc_center[0] + r * math.cos(math.radians(degree))
            arcy = arc_center[1] + r * math.sin(math.radians(degree))
            arc_points.append((arcx, arcy))
        self.drawing.add(self.drawing.polyline(arc_points))
        self.drawing.add(self.drawing.add(self.drawing.rect(insert=(0, 0), size=(self.width, self.height))))
        self.drawing.save(filename)




JupiterSign()