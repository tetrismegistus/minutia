import io

import imageio


class Animation:
    def __init__(self, outfile='animation.gif', duration=.01):
        self._frames = []
        self._outfile = outfile
        self._duration = duration

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

        imageio.mimsave('{}animated.gif'.format(self._outfile), images, duration=self._duration)

