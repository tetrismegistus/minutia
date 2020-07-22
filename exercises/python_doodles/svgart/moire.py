import svgwrite


def write_moire_layer(filename, width=1024, height=768, rangetuple=(10, 300, 5),
                      xdelta=0, ydelta=0):
    drawing = svgwrite.Drawing(filename, profile='full', size=(width, height))
    drawing.fill('none')
    drawing.stroke('black')
    for radius in range(*rangetuple):
        drawing.add(drawing.ellipse(center=(width/2, height/2), r=(radius - xdelta,
                                                                   radius - ydelta)))
    drawing.save(filename)



write_moire_layer('layer_3.svg', xdelta=10)
