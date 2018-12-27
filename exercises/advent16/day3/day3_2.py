"""
    --- Part Two ---

    Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups
    of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

    For example, given the following specification, numbers with the same hundreds digit would be part of the same
    triangle:

    101 301 501
    102 302 502
    103 303 503
    201 401 601
    202 402 602
    203 403 603
    In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

    Your puzzle answer was 1544.

"""


class ListWorker(object):
    def __init__(self, file_name='input.txt'):
        super().__init__()
        self.file_name = file_name
        self.file_lines = [line.rstrip('\n') for line in open(file_name)]
        self.true_triangles = 0
        self.work_lines()

    def work_lines(self):
        triangles = [[], [], []]
        line_groupings = 0

        for line in self.file_lines:
            line_groupings += 1
            lengths = line.split()
            for x in range(3):
                triangles[x].append(lengths[x])

            if line_groupings % 3 == 0:
                self.work_groupings(triangles)
                triangles = [[], [], []]

    def work_groupings(self, grouping):
        for group in grouping:
            this_set = NumberSet(group).is_triangle
            if this_set:
                self.true_triangles += 1


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

print(ListWorker().true_triangles)