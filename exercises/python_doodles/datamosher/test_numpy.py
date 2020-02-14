from random import randint

from PIL import Image
import numpy as np


def rgb_shift(im: np.array, offset: int, source_channel: int = None,
              target_channel: int = None, rows: bool = True, columns: bool = False):
    """
    :param im:  numpy array representing an image
    :param offset: the offset to shift the band by
    :param source_channel: the color band to move from
    :param target_channel: the color band to move to
    :param rows: shift rows
    :param columns: shift columns
    :return:
    """

    if source_channel is None:
        source_channel = randint(0, 2)
    if target_channel is None:
        target_channel = randint(0, 2)

    if columns:
        loffset = offset
        for column in range(im.shape[1]):
            if (loffset + column) >= im.shape[1]:
                loffset -= im.shape[1]

            source_band = im[:, column, source_channel]
            target_band = im[:, column + loffset, target_channel]
            im[:, column, source_channel] = target_band
            im[:, column + loffset, target_channel] = source_band

    if rows:
        loffset = offset
        for row in range(im.shape[0]):
            if (loffset + row) >= im.shape[0]:
                loffset -= im.shape[0]

            source_band = im[row, :, source_channel]
            target_band = im[row + loffset, :, target_channel]
            im[row, :, source_channel] = target_band
            im[row + loffset, :, target_channel] = source_band



def demo():
    im = np.array(Image.open('apt.jpg'))
    rgb_shift(im, 200, 0, 2, rows=False, columns=True)
    Image.fromarray(im).save('testnumpy1.jpg')
    im = np.array(Image.open('apt.jpg'))
    rgb_shift(im, 200, 0, 2, rows=True, columns=False)
    Image.fromarray(im).save('testnumpy2.jpg')
    im = np.array(Image.open('apt.jpg'))
    rgb_shift(im, 200, 0, 2, rows=True, columns=True)
    Image.fromarray(im).save('testnumpy3.jpg')

demo()