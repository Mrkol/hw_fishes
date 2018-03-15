from abc import ABCMeta, abstractmethod, abstractproperty
import itertools
import io
import re

class CellularAutomata:
    def __init__(w = 0, h = 0):
        self.width = w
        self.height = h
        self.field = [['_' for i in range(0, w)] for j in range(0, h)]
        self.rules = []

    def Step(self):
        newfield = self.field
        for i in range(0, self.width)
            for j in range(0, self.height)
                area = islice(cycle(self.field), j - 1, j + 1)
                area = islice(cycle(area), i - 1, i + 1)
                area = chain.from_iterable(area)
                area = list(area)
                area = area[0:3] + area[5] + area[6:9] + area[3]
                area = ''.join(area)

                for rule in rules:
                    if rule[0] == self.field[j][i] and rule[2].match(area):
                        newfield = rule[1]
                        break
        self.field = newfield

    def Set(self, x, y, state):
        self.field[y][x] = state

    def Get(self, x, y):
        return self.field[y][x]

    def FastForward(self, n):
        for i in range(0, n):
            self.Step()

    def ReadRules(self, textstream):
        self.rules = []
        for line in textstream:
            words = line.split()
            self.rules += (words[0], words[1], re.compile(' '.join(words[2:])))

    def ReadState(self, textstream):
        self.field = []
        for line in textstream:
            self.field += []
            for symbol in line:
                self.field[-1] += symbol


    def WriteState(self, textstream):
        textstream.write(str(self))
    
    def __str__(self):
        string = ""
        for row in field:
            for state in row:
                string += str(state)
            string += '\n'
        return string.strip()
