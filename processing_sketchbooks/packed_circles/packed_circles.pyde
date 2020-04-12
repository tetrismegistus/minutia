SIZE = 500


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @staticmethod
    def distance(point1, point2):
        xd = point1.x - point2.x
        yd = point1.y - point2.y
        return sqrt(xd ** 2 + yd ** 2)
    
    @staticmethod
    def random():
        x = random(0, width)
        y = random(0, height)
        return Point(x, y)
        
class Circle():
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center
        
    def render(self):
        fill(self.radius, 0, 0)
        ellipse(self.center.x,
                self.center.y,
                self.radius*2,
                self.radius*2)
        fill(0)
        
    @staticmethod
    def distance(circle1, circle2):
        d = Point.distance(circle1.center,
                           circle2.center)
        return d - (circle1.radius + circle2.radius)
    
    def mouse_distance(self):
        d = Point.distance(self.center, Point(mouseX, mouseY))
        return d
        
    
    @staticmethod
    def random():
        radius = random(5, 255)
        return Circle(radius, Point.random())


def pack_circles(attempts):
    circles = []
    for i in range(0, attempts):
        circle = Circle.random()
        collides = False
        for c in circles:
            if Circle.distance(c, circle) < 0:
                collides = True
                break
        if not collides:
            circles.append(circle)
    return circles


def setup():
    size(1024, 768)
    fill(0)
    noStroke()
    frameRate(0)
    draw()
    
def draw():
    clear()
    background(255)
    circles = pack_circles(50000)
    for circle in circles:
        if circle.mouse_distance() < 100:
            circle.radius += 1
        circle.render()
    
    
    
    
