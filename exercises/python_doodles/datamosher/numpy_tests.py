import numpy as np
from PIL import Image


def test_shift(im, sc=0, tc=2):
    new_im = im.copy()
    source_channel = sc
    target_channel = tc
    new_im[:, :, target_channel] = im[:, :, source_channel]
    new_im[:, :, source_channel] = im[:, :, target_channel]
    return new_im


def open_image(filename):
    im = Image.open(filename)
    return np.array(im)


def save_img(filename, matrix):
    i = Image.fromarray(matrix)
    i.save(filename)


def main():
    i = open_image('heather.jpg')
    i = test_shift(i, 1, 2)
    save_img('numpy.jpg', i)


if __name__ == '__main__':
    main()
