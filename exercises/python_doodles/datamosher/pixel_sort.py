import enum

from PIL import Image, ImageDraw


class mode(enum.Enum):
    BLACK = 0
    BRIGHTNESS = 1
    WHITE = 2


class PixelSort:
    def __init__(self, infile_name, mode, iterations=1, black_value=777216, brightness_value=60,
                 white_value=3777216):
        # orig_white 3777216
        self.filename = infile_name
        self.img = Image.open(infile_name)
        self.mode = mode
        self.iterations = iterations
        self.black_value = black_value
        self.white_value = white_value
        self.brightness_value = brightness_value
        self.w, self.h = self.img.size

    def sort_pixels(self):
        for x in range(self.iterations):
            column = 0
            row = 0

            while column < self.w - 1:
                pixels = self.sort_column(column)
                column += 1
                self.img.putdata(pixels)
            print('Column finished')

            while row < self.h - 1:
                pixels = self.sort_row(row)
                row += 1
                self.img.putdata(pixels)
            print('Row finished')

        self.img.save('SORTED' + self.filename)

    def sort_row(self, row):
        y = row
        x = 0
        xend = 0
        pixels = list(self.img.getdata())

        while xend < self.w - 1:
            if self.mode == mode.BLACK:
                x = self.get_first_not_black_x(x, y, pixels)
                xend = self.get_next_black_x(x, y, pixels)
            elif self.mode == mode.BRIGHTNESS:
                x = self.get_first_bright_x(x, y, pixels)
                xend = self.get_next_dark_x(x, y, pixels)
            elif self.mode == mode.WHITE:
                x = self.get_first_not_white_x(x, y, pixels)
                xend = self.get_next_white_x(x, y, pixels)

            if x < 0:
                break

            sort_length = xend - x
            unsorted = []

            for i in range(sort_length):
                unsorted.append(pixels[x + i + y * self.w])

            unsorted.sort()

            for i in range(sort_length):
                pixels[x + i + y * self.w] = unsorted[i]

            x = xend + 1
        return pixels

    def sort_column(self, column):
        x = column
        y = 0
        yend = 0
        pixels = list(self.img.getdata())

        while yend < self.h - 1:
            if self.mode == mode.BLACK:
                y = self.get_first_not_black_y(x, y, pixels)
                yend = self.get_next_black_y(x, y, pixels)
            elif self.mode == mode.BRIGHTNESS:
                y = self.get_first_bright_y(x, y, pixels)
                yend = self.get_next_dark_y(x, y, pixels)
            elif self.mode == mode.WHITE:
                y = self.get_first_not_white_y(x, y, pixels)
                yend = self.get_next_white_y(x, y, pixels)

            if y < 0:
                break

            sort_length = yend - y
            unsorted = []

            for i in range(sort_length):
                unsorted.append(pixels[x + (y + i) * self.w])

            unsorted.sort()

            for i in range(sort_length):
                pixels[x + (y + i) * self.w] = unsorted[i]

            y = yend + 1

        return pixels

    def get_next_white_y(self, x, y, pixels):
        y += 1
        if y < self.h:
            while rgb2int(*pixels[x + y * self.w]) < self.white_value:
                y += 1
                if y >= self.h:
                    return self.h - 1
        return y - 1

    def get_next_black_y(self, x, y, pixels):
        y += 1
        if y < self.h:
            while rgb2int(*pixels[x + y * self.w]) > self.black_value:
                y += 1
                if y >= self.h:
                    return self.h - 1

        return y - 1

    def get_first_not_white_y(self, x, y, pixels):
        if y < self.h:
            while rgb2int(*pixels[x + y * self.w]) > self.white_value:
                y += 1
                if y >= self.h:
                    return -1
        return y

    def get_first_not_black_y(self, x, y, pixels):
        if y < self.h:
            while rgb2int(*pixels[x + y * self.w]) < self.black_value:
                y += 1
                if y >= self.h:
                    return -1
        return y

    def get_next_dark_y(self, x, y, pixels):
        y += 1
        if y < self.h:
            while self.brightness(pixels[x + y * self.w]) > self.brightness_value:
                y += 1
                if y >= self.h:
                    return self.h -1
        return y - 1

    def get_first_bright_y(self, x, y, pixels):
        if y < self.h:
            while self.brightness(pixels[x + y * self.w]) < self.brightness_value:
                y += 1
                if y >= self.h:
                    return -1
        return y

    def get_next_white_x(self, x, y, pixels):
        x += 1
        while rgb2int(*pixels[x + y * self.w]) < self.white_value:
            x += 1
            if x >= self.w:
                return self.w - 1
        return x - 1

    def get_first_not_white_x(self, x, y, pixels):
        while rgb2int(*pixels[x + y * self.w]) > self.white_value:
            x += 1
            if x >= self.w:
                return -1
        return x

    def get_next_dark_x(self, x, y, pixels):
        x += 1
        while self.brightness(pixels[x + y * self.w]) > self.brightness_value:
            x += 1
            if x >= self.w:
                return self.w - 1
        return x - 1

    def get_first_bright_x(self, x, y, pixels):
        while self.brightness(pixels[x + y * self.w]) < self.brightness_value:
            x += 1
            if x >= self.w:
                return -1
        return x

    def get_next_black_x(self, x, y, pixels):
        x += 1
        while rgb2int(*pixels[x + y * self.w]) > self.black_value:
            x += 1
            if x >= self.w:
                return self.w - 1
        return x

    def get_first_not_black_x(self, x, y, pixels):
        while rgb2int(*pixels[x + y * self.w]) < self.black_value:
            x += 1
            if x >= self.w:
                return -1
        return x

    def brightness(self, pixels):
        return 1


def rgb2int(r, g, b, a=None):
    return int('{:02x}{:02x}{:02x}'.format(r, g, b), 16)


def main():
    ps = PixelSort('gorey.jpg', mode.BLACK, iterations=1)
    ps.sort_pixels()


if __name__ == '__main__':
    main()
