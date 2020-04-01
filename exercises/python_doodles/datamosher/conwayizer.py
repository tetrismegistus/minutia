from enum import Enum
import random

import numpy as np
from PIL import Image
from scipy.ndimage import convolve
import imageio


class State(Enum):
    ALIVE = 1
    DEAD = 2


class Cell:
    SCALE = {0: (0, 0, 0),
             1: (155, 61, 17),
             2: (177, 70, 20),
             3: (200, 80, 24),
             4: (222, 89, 28),
             5: (223, 103, 42),
             6: (225, 117, 61),
             7: (227, 134, 84),
             8: (255, 0, 0)}

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.fetidness = len(self.SCALE) - 1
        self.state = state

    @property
    def color(self):
        if self.state == State.ALIVE:
            return 120, 112, 11
        else:
            return Cell.SCALE[self.fetidness]

    def decay(self):
        if self.fetidness > 0:
            self.fetidness = self.fetidness - 1


class Universe:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_matrix = [[Cell(x, y, random.choice([State.ALIVE, State.DEAD, State.DEAD]))
                            for x in range(width)]
                            for y in range(height)]


def conwayize(img_array, universe):
    h, w = img_array.shape

    img_copy = np.copy(img_array)
    new_image_array = Image.new('RGB', (w, h))
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
                universe.cell_matrix[idx][idy].state = State.ALIVE
                universe.cell_matrix[idx][idy].fetidness = len(Cell.SCALE) - 1
            else:
                img_copy[idx][idy] = 0
                if universe.cell_matrix[idx][idy].state == State.DEAD:
                    universe.cell_matrix[idx][idy].decay()
                else:
                    universe.cell_matrix[idx][idy].state = State.DEAD

            new_image_array.putpixel((idy - 1, idx - 1), universe.cell_matrix[idx][idy].color)

    return new_image_array, img_copy


def main():
    pil_img = Image.open('drump.jpg')
    image_pil_conv = pil_img.convert('1', dither=Image.FLOYDSTEINBERG)
    one_bit_array = np.asarray(image_pil_conv, dtype=np.int8)
    universe = Universe(image_pil_conv.width, image_pil_conv.height)
    iterations = 1000
    mp4 = imageio.get_writer('agent_orange.mp4', fps=75)

    for _ in range(25):
        mp4.append_data(np.asarray(pil_img))    # display the first image for longer

    image_pil_conv, one_bit_array = conwayize(one_bit_array, universe)
    for _ in range(25):
        mp4.append_data(np.asarray(image_pil_conv))    # display the first image for longer

    image_pil_conv, one_bit_array = conwayize(one_bit_array, universe)
    for _ in range(25):
        mp4.append_data(np.asarray(image_pil_conv))  # display the first image for longer

    image_pil_conv, one_bit_array = conwayize(one_bit_array, universe)
    for _ in range(25):
        mp4.append_data(np.asarray(image_pil_conv))  # display the first image for longer

    image_pil_conv, one_bit_array = conwayize(one_bit_array, universe)
    for _ in range(25):
        mp4.append_data(np.asarray(image_pil_conv))  # display the first image for longer

    image_pil_conv, one_bit_array = conwayize(one_bit_array, universe)
    for _ in range(25):
        mp4.append_data(np.asarray(image_pil_conv))  # display the first image for longer

    image_pil_conv, one_bit_array = conwayize(one_bit_array, universe)
    for _ in range(25):
        mp4.append_data(np.asarray(image_pil_conv))  # display the first image for longer

    for x in range(iterations):
        image_pil_conv, one_bit_array = conwayize(one_bit_array, universe)
        mp4.append_data(np.asarray(image_pil_conv))

    mp4.close()


if __name__ == '__main__':
    main()
