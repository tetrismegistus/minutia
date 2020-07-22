import svgwrite
from math import sin, cos

dwg = svgwrite.Drawing('test.svg', profile='full', size=(400, 800))
dwg.add(dwg.circle(center=(400/2, 800/2), r=10, fill='white', stroke='black'))

dwg.save()