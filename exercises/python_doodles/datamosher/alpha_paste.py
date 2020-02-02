from random import randint

import argparse

from PIL import Image


def main(args):
    img = Image.open(args.file1)
    w, h = img.size
    foreground = Image.new('RGBA', size=(w, h))
    background = Image.open(args.file2)
    pixels = list(img.getdata())
    new_pixels = list(foreground.getdata())
    for i, p in enumerate(pixels):
        new_pixels[i] = (p[0], p[1], p[2], 175)
    foreground.putdata(new_pixels)
    background.paste(foreground, (0, 0), foreground)
    background.save('fuzzed.png')
    background.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("file1", help="Filename to process")
    parser.add_argument("file2", help="Filename to process")
    arguments = parser.parse_args()
    main(arguments)
