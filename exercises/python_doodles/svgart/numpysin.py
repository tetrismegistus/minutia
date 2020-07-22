import numpy as np
import svgwrite

time = np.arange(1, 100, 1)
amplitude =np.sin(time)

points = []
for idx, x in enumerate(time):
    points.append((int(x), int(amplitude[idx] * 10)))

drawing = svgwrite.Drawing('test.svg', profile='full')
drawing.stroke('black')
drawing.fill('none')
drawing.add(drawing.polyline(points))
drawing.save('test.svg')