#! /usr/bin/env python3

import copy, os, time, csv, random, curses
from curses import wrapper

class window(object):
    def __init__(self, frame, height, width):
        self.frame = True
        self.height = 
        self.width = 

class cell(object):
    def __init__(self, contains_life):
        self.live_neighbors = 0
        self.contains_life = False
        self.generation = 0

class board(object):
    def __init__(self):
        self.matrix = [[self.populate_field() for x in range(wh[1] - 2)] for y in range(wh[0] - 2)]

    def populate_field(self, percent=50):
        return random.randrange(100) < percent 

    def fill(self):
        pass

    def tick(self):
        pass
