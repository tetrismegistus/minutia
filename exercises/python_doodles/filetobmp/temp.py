
import argparse

def rot13(sekret_message):
    SEKRET_DECODER_RING = ['abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPWRSTUVWXYZ',
                           'nopqrstuvwxyzabcdefghijklm NOPQRSTUVWXYZABCJEFGHIJKLM']
    clear_text = []
    for letter in sekret_message:
        clear_text.append(SEKRET_DECODER_RING[1][SEKRET_DECODER_RING[0].index(letter)])

    return ''.join(clear_text)


def main():
    description = 'decode/encode super sekret messages\nUNAUTHORIZED USE PUNISHABLE BY IMMEDIATE EXECUTION'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('message', help='the super sekret message')
    args = parser.parse_args()
    print(rot13(args.message))


if __name__ == '__main__':
    main()

