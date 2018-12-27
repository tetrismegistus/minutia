import collections

'''
    --- Day 4: Security Through Obscurity ---

    Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of
    decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

    Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and
    a checksum in square brackets.

    A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with
    ties broken by alphabetization. For example:

    aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between
    x, y, and z, which are listed alphabetically.
    a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are
    listed alphabetically.
    not-a-real-room-404[oarel] is a real room.
    totally-real-room-200[decoy] is not.
    Of the real rooms from the list above, the sum of their sector IDs is 1514.

    What is the sum of the sector IDs of the real rooms?

    Your puzzle answer was 137896.
'''


class Room(object):
    def __init__(self, name):
        super().__init__()
        self.name = name.split('-')
        self.sector_and_checksum = self.name.pop(-1)
        self.sector_digit = ''
        self.checksum = ''
        self.name = ''.join(self.name)
        self.get_sector_and_checksum()
        self.letter_frequency = collections.Counter(self.name).most_common()
        self.letter_frequency = sorted(self.letter_frequency, key=lambda x: (-x[1], x[0]))
        self.letter_frequency = self.letter_frequency[:5]
        self.checkstring = ''.join([i[0] for i in self.letter_frequency])

    def get_sector_and_checksum(self):
        for char in self.sector_and_checksum:
            try:
                self.sector_digit = int(str(self.sector_digit) + str(char))
            except ValueError:
                pass

            try:
                if str(char).isalpha():
                    self.checksum += str(char)
            except ValueError:
                pass

    def check_validity(self):
        if self.checkstring == self.checksum:
            return True


class RoomList(object):
    def __init__(self, file_name='input.txt'):
        super().__init__()
        self.file_lines = [line.rstrip('\n') for line in open(file_name)]
        self.sum_of_rooms = 0
        self.work_list()

    def work_list(self):
        for line in self.file_lines:
            room = Room(line)
            if room.check_validity():
                self.sum_of_rooms += room.sector_digit


print(RoomList().sum_of_rooms)