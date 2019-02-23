import collections

'''
    --- Day 6: Signals and Noise ---

    Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol 
    in situations like this is to switch to a simple repetition code to get the message through.

    In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), 
    but the data seems quite corrupted - almost too badly to recover. Almost.

    All you need to do is figure out which character is most frequent for each position. For example, suppose you had 
    recorded the following messages:

    eedadn
    drvtee
    eandsr
    raavrd
    atevrs
    tsrnev
    sdttsa
    rasrtv
    nssdts
    ntnada
    svetve
    tesnvt
    vntsnd
    vrdear
    dvrsen
    enarar
    
    The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these 
    characters returns the error-corrected message, easter.

    Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

'''


file_name = 'input.txt'
file_lines = [line.rstrip('\n') for line in open(file_name)]

num_list = []
for char in range(len(file_lines[0])):
    num_list.append([])

for line in file_lines:
    for char, index in zip(line, range(len(line))):
        num_list[index].append(char)
    
for column in num_list:
    print(collections.Counter(column).most_common()[0][0], end='')
    
print()
