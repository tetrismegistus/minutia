import svgwrite

from PIL import Image


def get_dithered_image(filename):
    img = Image.open(filename)
    img = img.convert('1', dither=Image.FLOYDSTEINBERG)
    return img


def raster_to_vector_line_coords(dithered_image):
    lines = []
    for y in range(dithered_image.height):
        startx = 0
        endx = 0
        drawing = False
        for x in range(dithered_image.width):
            if dithered_image.getpixel((x, y)) == 0:
                if drawing:
                    endx = x
                else:
                    startx = x
                    endx = x
                    drawing = True
            else:
                if drawing:
                    drawing = False
                    lines.append([(startx, y), (endx, y)])

    return lines


def create_vector_image(list_of_line_tuples, filename):
    drawing = svgwrite.Drawing(f"output/{filename}")
    drawing.stroke('black')
    drawing.fill('none')
    for line in list_of_line_tuples:
        drawing.add(drawing.line(line[0], line[1]))
    drawing.save()


def main():
    dithered = get_dithered_image('justface.png')
    dithered.save('justface_dithered.png')
    lines = raster_to_vector_line_coords(dithered)
    create_vector_image(lines, 'raster.svg')


if __name__ == '__main__':
    main()
