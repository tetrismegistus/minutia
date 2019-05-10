import hashlib
import sys
import random
import os

'''
    --- Part Two ---

    As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism.
    Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny 
    engineers have worked out a better solution.

    Instead of simply filling in the password from left to right, the hash now also indicates the position within the 
    password to fill. You still look for hashes that begin with five zeroes; however, now, the sixth character 
    represents the position (0-7), and the seventh character is the character to put in that position.

    A hash result of 000001f means that f is the second character in the password. Use only the first result for each 
    position, and ignore invalid positions.

    For example, if the Door ID is abc:

    The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
    In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an 
    invalid position (8).
    The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 
    4: _5__e___.
    You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.

    Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a 
    cinematic "decrypting" animation.

    Your puzzle answer was 694190cd.

    Both parts of this puzzle are complete! They provide two gold stars: **

'''


class MovieDecrypter(object):

    def __init__(self, prefix='uqwqemis'):
        os.system('clear')
        self.prefix = prefix
        self.password = [[],[],[],[],[],[],[],[]]
        self.solved = 0
        self.solver()
        print()
    
    def solver(self):
        index = 0
        while self.solved <= 7:
            if index % 10 == 0:
                self.print_routine()
            index += 1
            string_to_hash = self.prefix + str(index)
            hash_object = hashlib.md5(string_to_hash.encode('utf-8'))
            hex = hash_object.hexdigest()[:7]
            if hex[:5] == '00000':
                self.check_hash(hex[5], hex[6])
                self.print_routine()

    def check_hash(self, position, letter):
        try:            
            if not self.password[int(position)]:
                self.password[int(position)] = letter
                self.solved += 1 
        except IndexError:
            pass
        except ValueError:
            pass

    def print_routine(self):
        print_list = []
        for char in self.password:
            if char: 
                print_list.append(char)
            else:
                print_list.append(random.choice('!@#$%^&*()_-+={}\|/?.><,`~'))
        
        print_list = ''.join(print_list) 
        sys.stdout.write("\r %s" % print_list)
        sys.stdout.flush()
            


MovieDecrypter()
