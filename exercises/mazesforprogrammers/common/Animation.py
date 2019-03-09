import io

import imageio

from common import runtimedefs as rd


class Animation:
    def __init__(self):
        self._frames = []

    @property
    def frames(self):
        return self._frames

    @frames.setter
    def frames(self, img):
        with io.BytesIO() as output:
            img.save(output, format="GIF", quality=30)
            self._frames.append(output.getvalue())

    def save_gif(self, pause=20, reverse=False):
        images = [imageio.imread(f) for f in self._frames]
        if not reverse:
            images += [images[-1] for _ in range(pause)]
        if reverse:
            rrw = images.copy()
            rrw.reverse()
            images += rrw

        imageio.mimsave('{}animated.gif'.format(rd.DIRS['output']), images, duration=.00000000001)
