from PIL import Image, ImageDraw
from random import choice

from animation import Animation


class elemCa:
    def __init__(self, ruleset=30, filename=None, bg=(96, 167, 169), fg=(255, 255, 255), imw=200, imh=200,
                 animation=None):
        self.bg = bg
        self.fg = fg
        self.imw = imw
        self.imh = imh
        self.ca_img = Image.new('RGB', (imw, imh), color=bg)
        self.drawing = ImageDraw.Draw(self.ca_img)
        self.w = 2
        self.rows = imh
        self.cols = imw
        self.cells = []
        self.ruleset = [int(i) for i in format(ruleset, '08b')]
        self.filename = filename
        self.animation = animation
        self.generate()
        self.draw()

    def rules(self, a, b, c):
        return self.ruleset[7 - (4 * a + 2 * b + c)]

    def generate(self):

        for r in range(self.rows):
            self.cells.append([])
            for c in range(self.cols):
                self.cells[r].append(choice([0, 0, 0, 0, 1]))
        self.cells[0][self.cols // 2] = 1
        self.cells[0][0] = 1

        for i, row in enumerate(self.cells):
            for j in range(1, len(row) - 1):
                left = row[j - 1]
                me = row[j]
                right = row[j + 1]
                if i < len(self.cells) - 1:
                    self.cells[i + 1][j] = self.rules(left, me, right)

    def draw(self):
        for i, cell in enumerate(self.cells):
            for j, v in enumerate(cell):
                if v == 1:
                    f = self.fg
                else:
                    f = self.bg
                x = j * self.w - (self.cols * self.w - self.imw) / 2
                y = self.w * i

                bbox = [x, y, x + self.w, y + self.w]
                self.drawing.rectangle(bbox, f)
            if self.animation is not None:
                self.animation.frames = self.ca_img.copy()

        if self.animation is not None:
            self.animation.save_gif()

        if self.filename is not None:
            self.ca_img.save(self.filename)


rule = 225
elemCa(rule, f'{rule}.png', (255, 128, 255), (0, 0, 0), imw=500, imh=500,
       animation=Animation(f'{rule}.gif', duration=.0001))
