import math
import sys


class Bitmap:
    def __init__(self, pixel_array, w):
        self.w = w
        self.pixel_array = pixel_array
        self.dib_header = self.create_dib_header()
        self.bmp_header = self.create_bmp_header()
        self.bmp = self.bmp_header + self.dib_header + self.pixel_array

    def create_bmp_header(self):
        id_field = b'BM'
        size = len(self.pixel_array) + 54
        size = size.to_bytes(4, byteorder='little')
        unused = b'\x00\x00'
        pix_array_offset = 14 + 40
        pix_array_offset = pix_array_offset.to_bytes(4, byteorder='little')
        return id_field + size + unused + unused + pix_array_offset

    def create_dib_header(self):
        dib_size = b'\x28\x00\x00\x00'
        width_of_bitmap = self.w.to_bytes(4, byteorder='little')
        height_of_bitmap = int(int(len(self.pixel_array) / 3) / self.w)
        height_of_bitmap = height_of_bitmap.to_bytes(4, byteorder='little')
        planes = b'\x01\x00'              # 1 plane
        bits = b'\x18\x00'                # 24 bits for color
        compression = b'\x00\x00\x00\x00'  # no compression
        size_of_data = len(self.pixel_array).to_bytes(4, byteorder='little')
        print_resolution = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        palette = b'\x00\x00\x00\x00'
        color_importance = b'\x00\x00\x00\x00'
        result = dib_size + width_of_bitmap + height_of_bitmap + planes + bits + compression + size_of_data
        result += print_resolution + palette + color_importance
        return result

    def save(self, filename):
        with open(filename, 'wb') as f:
            f.write(self.bmp)


def read_into_bytearray(filename):
    with open(filename, 'rb') as f:
        contents = f.read()
    return bytearray(contents)


def pad_byte_array(ba, grouping):
    padding_length = (math.ceil(len(ba) / grouping) * grouping) - len(ba)
    return ba + b'\x00' * padding_length


def approximate_square_mult_4(size):
    square = math.sqrt(size)
    w = math.ceil(square)
    h = w
    while w % 4 != 0:
        w += 1
    return w, h


def create_image(infile, outfile):
    file_as_bytes = read_into_bytearray(infile)
    w, h = approximate_square_mult_4(int(len(file_as_bytes) / 3))
    padded_pixel_array = pad_byte_array(file_as_bytes, w)
    bmp = Bitmap(padded_pixel_array, w)
    bmp.save(outfile)


def main():
    if len(sys.argv) < 2:
        print("Usage: [bmpInTheNIght.py] [inputfile] [output]")
        print("       where [inputfile] is a valid file/path")
        print("       and [output] is a user writeable file/path")
    else:
        create_image(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
