#!/usr/bin/env python3
import collections
import random
import os
from functools import reduce

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # French deck class from Fluent Python
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = '♠ ♦ ♣ ♥'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, key, value):
        self.set_card(key, value)

    def pop(self):
        card = self._cards.pop()
        return card

    def set_card(self, position, card):
        self._cards[position] = card


class Hand:
    def __init__(self, two_cards):
        self._hand = []
        self._illustrations = []
        self._score = 0
        self.h_init(two_cards)

    def h_init(self, two_cards):
        for c in two_cards:
            self.append(c)

    def __getitem__(self, position):
        return self._hand[position]

    def append(self, card):
        self._illustrations.append(self.illustrate_card(card))
        self._hand.append(card)
        self.calculate_score()

    def illustrate_card(self, card):
        return ['┌────┐',
                '│{}   │'.format(card.suit),
                '│ {} │'.format(card.rank.rjust(2)),
                '│   {}│'.format(card.suit),
                '└────┘']
    
    def print_cards(self):
        for card in zip(*self._illustrations):
            print(' '.join(card))

    def get_score(self):
        return self._score

    def get_values(self):
        face_cards = 'J Q K'.split()
        values = []
        for c in self:
            if c.rank in face_cards:
                values.append(10)
            elif c.rank == 'A':
                values.append(1)
            else:
                values.append(int(c.rank))
        return values

    def calculate_score(self):
        # this is our list of scores for the hand, we start with aces = 1
        card_values = self.get_values()
        
        # We're creating a list of scores to choose from.
        # for i in range(0, card_values.count(1) + 1
        # For every instance of an ace in the hand, we want to use the reduce function.
        # For every ace, we will progressively add 10, except the first time
        # when assume every ace is equal to 1 (10 * i == 0). 
        # https://lists.gt.net/python/python/150242#150242
        scores = [(reduce(lambda card1, card2: card1+card2,card_values, 0) + 10 * i) 
                  for i in range(0, card_values.count(1) + 1)]
        
        # now I'm selecting all scores that aren't a bust
        possibilities = [score for score in scores if score <= 21]
        # and either busting or returning the largest value
        if len(possibilities) == 0:
            self._score = min(scores)
        else:
            self._score = max(possibilities)


class ComputerHand(Hand):
    def __init__(self, two_cards):
        Hand.__init__(self, two_cards)
        _hole_pic = ['┌────┐', 
                     '│░░░░│', 
                     '│░░░░│',
                     '│░░░░│',
                     '└────┘']
        self._illustrations[1] = _hole_pic
        self._revealed = False
        if self._score == 21:
            self.reveal_hole()
    
    def reveal_hole(self):
        self._illustrations[1] = self.illustrate_card(self._hand[1])
        self._revealed = True

    def get_score(self):
        if self._revealed:
            return self._score
        else:
            return '??'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    os.system('pause' if os.name == 'nt' else "/bin/bash -c 'read -s -n 1 -p \"Press any key to continue...\"'")
    print('')


def get_input(prompt, options):
    while True:
        choice = input(prompt)
        if choice.upper() not in options:
            print('Valid options are:')
            [print(x, end=' ') for x in options]
            print('')
        else:
            return choice.upper()


def print_all(phand, chand, message=''):
    clear_screen()    
    print('Your hand:')
    phand.print_cards()
    print('')
    print('Computer hand:')
    chand.print_cards()
    print('')
    print(message)
    print('')
    print('Player Score:   ', phand.get_score())
    print('Computer_score: ', chand.get_score())
    print('')


def dealer_turn(cdeck, chand, phand):
    chand.reveal_hole()
    print_all(phand, chand)
    pause()
    continue_play = True
    while continue_play:
        continue_play = chand.get_score() < 17
        if chand.get_score() == 21:
            message = 'Dealer blackjack!'
        elif chand.get_score() > 21:
            message = 'The dealer busts!'
        elif not continue_play:
            message = 'The dealer stays.'
        else:
            chand.append(cdeck.pop())
            message = 'The dealer hits.'
        print_all(phand, chand, message)
        pause()


def play():
    deck = FrenchDeck()
    random.shuffle(deck)
    player_hand = Hand([deck.pop(), deck.pop()])
    comp_hand = ComputerHand([deck.pop(), deck.pop()])
    continue_play = player_hand.get_score() < 21
    message = ''
    if not continue_play:
        message = 'Player blackjack!'
    print_all(player_hand, comp_hand, message)
    while continue_play:
        hit_or_fold = get_input('Do you want to HIT or STAY: ', ['HIT', 'STAY'])
        message = ''
        if hit_or_fold == 'HIT':
            player_hand.append(deck.pop())
            continue_play = player_hand.get_score() < 21
            message += 'Player hits'
            if player_hand.get_score() > 21:
                message += '\n and busts!'
            elif player_hand.get_score() == 21:
                message += '\n and gets a blackjack!'
            print_all(player_hand, comp_hand, message)
        else:
            print_all(player_hand, comp_hand, 'Player stays')
            continue_play = False
        if not continue_play:
            print('The computer will now play')
    pause()
    dealer_turn(deck, comp_hand, player_hand)


if __name__ == '__main__':
    play()

