import svgwrite
import pandas as pd
from math import sqrt
from itertools import tee


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class Sphere(Circle):
    def __init__(self, value, title, x, y, radius):
        super(Sphere, self).__init__(x, y, radius)
        self.value = value
        self.title = title


class Path:
    def __init__(self, start, end, name, value):
        self.start = start
        self.end = end
        self.name = name
        self.value = value


class Tree:
    def __init__(self, width=768, height=1024, radius=30, filename='Kircher.svg'):
        self.margin = radius
        self.drawing = svgwrite.Drawing(filename, profile='full', size=(width, height))
        self.path_width = 15
        self.width = width
        self.height = height
        self.backbone_radius = self.height // 4
        self.sphere_radius = radius
        self.spheres = self.get_spheres()
        self.paths = self.get_paths()
        self.draw_paths()
        self.draw_spheres()
        # self.write_names()
        self.drawing.save(filename)

    def get_spheres(self):
        df = pd.read_csv('spheres.csv')
        center_x = (self.width // 2) + self.margin
        center_length = self.backbone_radius * 4
        backbone = [Circle(center_x, c, self.backbone_radius)
                    for c in range(self.margin, center_length, self.backbone_radius)]
        balance = [1, 0, 6, 9]
        side_pillars = [2, 3, 4, 5, 7, 8]
        spheres = []

        for i, svalue in zip(backbone, balance):
            row = df[df['Value'] == svalue]
            spheres.append(Sphere(svalue, row.iloc[0]['Name'], i.x, i.y, self.sphere_radius))

        spheres.append(Sphere(10, 'Malkuth', center_x, self.margin + self.backbone_radius * 4, self.sphere_radius))

        for c1, c2 in pairwise(backbone):
            intersections = circle_intersection(c1, c2)
            for inter in intersections:
                svalue = side_pillars.pop(0)
                row = df.loc[df['Value'] == svalue]
                spheres.append(Sphere(svalue, row.iloc[0]['Name'], inter[0], inter[1], self.sphere_radius))

        return spheres

    def draw_spheres(self):
        for s in self.spheres:
            self.draw_circle(s)

    def draw_circle(self, circle):
        self.drawing.add(self.drawing.circle((circle.x,
                                              circle.y), r=circle.radius, fill="none", stroke="black"))



    def get_paths(self):
        path_dict = {sphere.value: sphere for sphere in self.spheres}
        df = pd.read_csv('paths.csv')

        def make_paths(row): return Path(path_dict[row['KStart']],
                                         path_dict[row['KEnd']],
                                         row['Name'],
                                         row['Value'])

        paths = df.apply(make_paths, axis=1)
        return paths

    def draw_paths(self):
        offset = self.sphere_radius / 4
        for p in self.paths:

            self.drawing.add(self.drawing.line(start=(p.start.x + offset, p.start.y + offset),
                                               end=(p.end.x + offset, p.end.y + offset),
                                               stroke='black'))

            self.drawing.add(self.drawing.line(start=(p.start.x - offset, p.start.y - offset),
                                               end=(p.end.x - offset, p.end.y - offset),
                                               stroke='black'))



def circle_intersection(circle1, circle2):
    # https://gist.github.com/xaedes/974535e71009fa8f090e
    # thanks!
    x1, y1, r1 = circle1.x, circle1.y, circle1.radius
    x2, y2, r2 = circle2.x, circle2.y, circle2.radius
    dx, dy = x2 - x1, y2 - y1
    d = euclidean_distance(x1, y1, x2, y2)

    if d > r1 + r2:
        return None  # circles are separate
    elif d < abs(r1 - r2):
        return None  # circle within another
    elif d == 0 and r1 == r2:
        return None  # circles are coincident

    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h = sqrt(r1 * r1 - a * a)
    xm = x1 + a * dx / d
    ym = y1 + a * dy / d
    xs1 = int(xm + h * dy / d)
    xs2 = int(xm - h * dy / d)
    ys1 = int(ym - h * dx / d)
    ys2 = int(ym + h * dx / d)

    return (xs1, ys1), (xs2, ys2)


def euclidean_distance(x1, y1, x2, y2):
    return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def main():
    Tree()


if __name__ == "__main__":
    main()


