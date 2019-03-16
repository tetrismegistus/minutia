from PIL import Image, ImageDraw


def downsample(infile, sample_rate=20, shrink=True, bgcolor=(255, 255, 255)):
    img = Image.open(infile)
    pixels = list(img.getdata())

    w, h = img.size
    pixels = [pixels[i * w:(i + 1) * w] for i in range(h)]

    if shrink:
        def rescale(x): return int(x / sample_rate) + 1
        image = Image.new('RGB', size=(rescale(w), rescale(h)), color=bgcolor)
    else:
        image = Image.new('RGB', size=(w, h), color=bgcolor)

    drawing = ImageDraw.Draw(image)

    for row in range(0, h, sample_rate):
        for col in range(0, w, sample_rate):
            r, g, b = pixels[row][col]
            if not shrink:
                drawing.rectangle([(col, row), (col + sample_rate, row + sample_rate)], fill=(r, g, b))
            else:
                drawing.point([(col / sample_rate, row / sample_rate)], fill=(r, g, b))

    return image