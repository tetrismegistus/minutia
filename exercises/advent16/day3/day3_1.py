#!/usr/bin/env python3

"""
    --- Day 3: Squares With Three Sides ---

    Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up
    this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for
    triangles.

    Or are they?

    The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't
    triangles. You can't help but mark the impossible ones.

    In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle"
    given above is impossible, because 5 + 10 is not larger than 25.

    In your puzzle input, how many of the listed triangles are possible?

    Your puzzle answer was 869.
"""


class NumberSet(object):
    def __init__(self, number_list):
        super().__init__()
        self.number_list = number_list
        self.is_triangle = None
        self.test_triangularity()

    def test_triangularity(self):
        for value, index in zip(self.number_list, list(range(3))):
            test_sum = int(self.number_list[(index - 1) % 3]) + int(self.number_list[(index + 1) % 3])
            if test_sum > int(value):
                self.is_triangle = True
            else:
                self.is_triangle = False
                break


class ListWorker(object):
    def __init__(self, file_name='input.txt'):
        super().__init__()
        self.file_name = file_name
        self.file_lines = [line.rstrip('\n') for line in open(file_name)]
        self.true_triangles = 0
        self.work_lines()

    def work_lines(self):
        for line in self.file_lines:
            lengths = line.split()
            this_set = NumberSet(lengths).is_triangle
            if this_set:
                self.true_triangles += 1

print(ListWorker().true_triangles)

