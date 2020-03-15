import io

import imageio


class Animation:
    def __init__(self, filename, quality=30, pause=5, duration=1):
        self._frames = []
        self.filename = filename
        self.quality = quality
        self.pause = pause
        self.duration = duration

    @property
    def frames(self):
        return self._frames

    @frames.setter
    def frames(self, img):
        with io.BytesIO() as output:
            img.save(output, format="GIF", quality=self.quality)
            self._frames.append(output.getvalue())

    def save_gif(self, reverse=False):
        images = [imageio.imread(f) for f in self._frames]
        if not reverse:
            images += [images[-1] for _ in range(self.pause)]
        if reverse:
            rrw = images.copy()
            rrw.reverse()
            images += rrw

        imageio.mimsave('animated.gif', images, duration=self.duration)

