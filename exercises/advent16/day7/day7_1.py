import re

'''
    --- Day 7: Internet Protocol Version 7 ---

    While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6
    is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

    An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence
    which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba.
    However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

    For example:

    abba[mnop]qrst supports TLS (abba outside square brackets).
    abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
    aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
    ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
    How many IPs in your puzzle input support TLS?

    Your puzzle answer was 118.
'''


class Address(object):
    def __init__(self, input_string):
        self.ip_address = input_string
        self.supports_TLS = 'unknown'
        self.hypernets = re.findall('\[.*?\]', self.ip_address)
        self.segments = re.split('\[.*?\]', self.ip_address)
        self.ip_checker()

    def ip_checker(self):
        for block in self.hypernets:
            has_hypernet = self.check_symmetry(block)
        
            if has_hypernet:
                self.supports_TLS = False
                return

        for segment in self.segments:
            if self.check_symmetry(segment):
                self.supports_TLS = True
                return
            else:
                self.supports_TLS = False

    def check_symmetry(self, input_string):
        segment = input_string
        for char, index in zip(segment, range(len(segment))):
            quad = segment[index:index + 4]

            # eliminate short strings or strings of repeating character
            if len(quad) != 4 or len(set(quad)) == 1:
                break
            bi1 = quad[:2]   # first half of quad
            bi2 = quad[2:]   # second half of quad
            bi2 = bi2[::-1]  # reverse the second half
            if bi1 == bi2:
                return True


if __name__ == '__main__':
    file_name = 'input.txt'
    file_lines = [line.rstrip('\n') for line in open(file_name)]
    count = 0
    for line in file_lines:
        if Address(line).supports_TLS:
            count += 1

    print(count)