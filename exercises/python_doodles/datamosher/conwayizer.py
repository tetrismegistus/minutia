import numpy as np
from PIL import Image
from scipy.ndimage import convolve

from animation import Animation


def conwayize(pil_img):
    img_array = np.asarray(pil_img, dtype=np.int8)

    img_copy = np.copy(img_array)
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    c = convolve(img_array, kernel, mode='constant')

    for idx, x in enumerate(c):
        for idy, y in enumerate(x):
            count = y
            alive = img_array[idx][idy]

            """                
            All other live cells die in the next generation. Similarly, all other dead cells stay dead.
            """
            rule1 = alive and count in range(2, 4)  # Any live cell with two or three neighbors survives.
            rule2 = not alive and count == 3  # Any dead cell with three live neighbors becomes a live cell.

            if rule1 or rule2:
                img_copy[idx][idy] = 1
            else:
                img_copy[idx][idy] = 0

    return Image.fromarray(img_copy.astype(np.bool))


def main():
    pil_img = Image.open('drump.jpg')
    image_pil_conv = pil_img.convert('1', dither=Image.FLOYDSTEINBERG)
    iterations = 300
    gif = Animation('drump.gif', duration=.25)
    gif.frames = pil_img
    gif.frames = image_pil_conv
    for x in range(iterations):
        image_pil_conv = conwayize(image_pil_conv)
        gif.frames = image_pil_conv

    gif.save_gif()


if __name__ == '__main__':
    main()

