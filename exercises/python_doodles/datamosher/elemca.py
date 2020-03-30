from PIL import Image, ImageDraw


class elemCa:
    def __init__(self, ruleset=30, filename='ca.png', bg=(0, 0, 0), fg=(255, 255, 255), imw=200, imh=200):
        self.bg = bg
        self.fg = fg
        self.imw = imw
        self.imh = imh
        self.ca_img = Image.new('RGB', (imw, imh))
        self.drawing = ImageDraw.Draw(self.ca_img)
        self.w = 2
        self.rows = 100
        self.cols = 100
        self.cells = []
        self.ruleset = [int(i) for i in format(ruleset, '08b')]
        self.filename = filename
        self.generate()
        self.draw()

    def rules(self, a, b, c):
        return self.ruleset[7 - (4 * a + 2 * b + c)]

    def generate(self):
        for r in range(self.rows):
            self.cells.append([])
            for c in range(self.cols):
                self.cells[r].append(0)
        self.cells[0][self.cols // 2] = 1

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
        self.ca_img.save(self.filename)


elemCa(57, '57.png', (255, 128, 255))
