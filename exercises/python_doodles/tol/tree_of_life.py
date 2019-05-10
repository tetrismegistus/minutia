from math import sqrt
from itertools import tee

from PIL import Image, ImageDraw
from rgb_colors import COLORS
import pandas as pd

from Animation import Animation


class Circle:
    def __init__(self, x, y, radius, color='black'):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color


class Sphere(Circle):
    def __init__(self, value, title, x, y, radius, color='black'):
        super(Sphere, self).__init__(x, y, radius, color=color)
        self.value = value
        self.title = title


class Path:
    def __init__(self, start, end, name, value, color='black'):
        self.start = start
        self.end = end
        self.name = name
        self.value = value
        self.color = color


class KircherTree:
    def __init__(self, width=400, height=800, radius=30, filename='Kircher.png', animation=None):
        self.margin = radius
        self.image = Image.new('RGB', (width + self.margin*2, height + self.margin*2), color=(0, 42, 76))
        self.drawing = ImageDraw.Draw(self.image)
        self.animation = animation
        self.path_width = 15
        self.width = width
        self.height = height
        self.backbone_radius = self.height // 4
        self.sphere_radius = radius
        self.spheres = self.get_spheres()
        self.paths = self.get_paths()
        self.draw_paths()
        self.draw_spheres()
        self.write_names()
        self.image.save(filename)

        if self.animation is not None:
            self.animation.save_gif()

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
            spheres.append(Sphere(svalue, row.iloc[0]['Name'], i.x, i.y, self.sphere_radius,
                                  row.iloc[0]['Mathers Combined']))

        spheres.append(Sphere(10, 'Malkuth', center_x, self.margin + self.backbone_radius * 4, self.sphere_radius,
                              'black'))

        for c1, c2 in KircherTree.pairwise(backbone):
            intersections = self.circle_intersection(c1, c2)
            for inter in intersections:
                svalue = side_pillars.pop(0)
                row = df.loc[df['Value'] == svalue]
                spheres.append(Sphere(svalue, row.iloc[0]['Name'], inter[0], inter[1], self.sphere_radius,
                                      row.iloc[0]['Mathers Combined']))

        return spheres

    def get_paths(self):
        path_dict = {sphere.value: sphere for sphere in self.spheres}
        df = pd.read_csv('paths.csv')

        def make_paths(row): return Path(path_dict[row['KStart']],
                                         path_dict[row['KEnd']],
                                         row['Name'],
                                         row['Value'],
                                         row['Mathers Combined'])

        paths = df.apply(make_paths, axis=1)

        return paths

    def draw_spheres(self):
        for s in self.spheres:
            self.draw_circle(s)
            if s.title == 'Malkuth':
                self.paint_malkuth(s)
            if self.animation:
                self.animation.frames = self.image

    def paint_malkuth(self, circle):
        slices = [(45, 315),
                  (315, 225),
                  (135, 225),
                  (45, 135)]
        colors = ['citrine', 'olive', 'russet', 'black']
        for c, s in zip(colors, slices):
            self.drawing.pieslice((circle.x - circle.radius,
                                   circle.y - circle.radius,
                                   circle.x + circle.radius,
                                   circle.y + circle.radius), s[0], s[1], fill=COLORS[c])

    def draw_circle(self, circle):
        self.drawing.ellipse((circle.x - circle.radius,
                              circle.y - circle.radius,
                              circle.x + circle.radius,
                              circle.y + circle.radius), fill=COLORS[circle.color])

    def draw_paths(self):
        for p in self.paths:
            self.drawing.line([(p.start.x, p.start.y), (p.end.x, p.end.y)], width=self.path_width, fill=COLORS[p.color])
            if self.animation:
                self.animation.frames = self.image

    def write_names(self):
        for p in self.paths:
            self.drawing.text(text=p.name, xy=[(p.start.x + p.end.x) / 2, p.start.y])
        for s in self.spheres:
            self.drawing.text(text=s.title, xy=[s.x, s.y])

    @staticmethod
    def pairwise(iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

    @staticmethod
    def euclidean_distance(x1, y1, x2, y2):
        return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

    @staticmethod
    def circle_intersection(circle1, circle2):
        # https://gist.github.com/xaedes/974535e71009fa8f090e
        # thanks!
        x1, y1, r1 = circle1.x, circle1.y, circle1.radius
        x2, y2, r2 = circle2.x, circle2.y, circle2.radius
        dx, dy = x2 - x1, y2 - y1
        d = KircherTree.euclidean_distance(x1, y1, x2, y2)

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


def main():
    KircherTree(animation=Animation('test.gif', duration=1))


if __name__ == "__main__":
    main()
