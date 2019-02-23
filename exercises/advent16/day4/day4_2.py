import collections

"""
    --- Part Two ---

    With all the decoy data out of the way, it's time to decrypt this list and get moving.

    The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right
    software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master
    cryptographer like yourself.

    To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector
    ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

    For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

    What is the sector ID of the room where North Pole objects are stored?
"""


class Room(object):
    def __init__(self, name):
        super().__init__()
        self.name = name.split('-')
        self.sector_and_checksum = self.name.pop(-1)
        self.truncated_name = list(self.name)
        self.sector_digit = ''
        self.checksum = ''
        self.truncated_name = ''.join(self.truncated_name)
        self.get_sector_and_checksum()
        self.letter_frequency = collections.Counter(self.truncated_name).most_common()
        self.letter_frequency = sorted(self.letter_frequency, key=lambda x: (-x[1], x[0]))
        self.letter_frequency = self.letter_frequency[:5]
        self.checkstring = ''.join([i[0] for i in self.letter_frequency])
        self.decoded_name = ''
        self.decode_room_name()

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

    def decode_room_name(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        cypher = []

        for word in self.name:
            for letter in word:
                index = alphabet.index(letter)
                cypher.append(alphabet[(index + self.sector_digit) % 26])
            cypher.append(" ")
        self.decoded_name = ''.join(cypher)


class RoomList(object):
    def __init__(self, file_name='input.txt'):
        super().__init__()
        self.file_lines = [line.rstrip('\n') for line in open(file_name)]
        self.real_rooms = []
        self.remove_decoys()
        self.list_real_room_names()

    def remove_decoys(self):
        for line in self.file_lines:
            room = Room(line)
            if room.check_validity():
                self.real_rooms.append(room)

    def list_real_room_names(self):
        for room in self.real_rooms:
            print(room.decoded_name, room.sector_digit)

RoomList()
