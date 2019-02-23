import re
import pdb

'''
    --- Part Two ---

    You would also like to know which IPs support SSL (super-secret listening).

    An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any
    square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences.
    An ABA is any three-character sequence which consists of the same character twice with a different character between
    them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab,
    respectively.

    For example:

    aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
    xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
    aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related,
    because the interior character must be different).
    zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz
    overlap).
    How many IPs in your puzzle input support SSL?

    Your puzzle answer was 260.
'''

class Address(object):
    def __init__(self, input_string):
        self.ip_address = input_string
        self.supports_SSL = False
        self.hypernets = re.findall('\[.*?\]', self.ip_address)
        self.supernets = re.split('\[.*?\]', self.ip_address)
        self.aba_triads = self.build_triads(self.supernets)
        self.bab_triads = self.build_triads(self.hypernets)
        self.ip_checker()

    def ip_checker(self):
        for aba in self.aba_triads:
            aba_has_symmetry = self.check_symmetry(aba)
            if aba_has_symmetry:
                for bab in self.bab_triads:
                    bab_has_symmetry = self.check_symmetry(bab)
                    if bab_has_symmetry is None:
                        bab_has_symmetry = []
                    paired_bab = set(aba_has_symmetry) == set(bab_has_symmetry)
                    difference = bab_has_symmetry != aba_has_symmetry
                    if paired_bab and difference:
                        self.supports_SSL = True
                        return

    def build_triads(self, input_list):
        segment_list = input_list
        triads = []
        for segment in segment_list:
            for char, index in zip(segment, range(len(segment))):
                triad = segment[index:index + 3]
                if len(triad) == 3 and len(set(triad)) != 1:
                    triads.append(triad)
        return triads

    def check_symmetry(self, input_string):
        triad = input_string
        if triad == triad[::-1]:
            return triad


if __name__ == '__main__':
    file_name = 'input.txt'
    file_lines = [line.rstrip('\n') for line in open(file_name)]
    count = 0
    for line in file_lines:
        if Address(line).supports_SSL:
            count += 1

    print(count)