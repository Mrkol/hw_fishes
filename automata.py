from abc import ABCMeta, abstractmethod, abstractproperty
from itertools import islice, cycle, chain 
import io
import re

class CellularAutomata:
    def __init__(self):
        self.field = []
        self.rules = []

    def Step(self):
        newfield = self.field
        for j in range(0, len(self.field)):
            for i in range(0, len(self.field[j])):
                h = len(self.field)
                w = len(self.field[0])
                area = islice(cycle(self.field), h + j - 1, h + j + 2)
                area = (islice(cycle(row), w + i - 1, w + i + 2) for row in area)
                area = chain.from_iterable(area)
                area = list(area)
                area = area[0:3] + area[5:6] + area[6:9][::-1] + area[3:4]
                area = ''.join(area)

                for rule in self.rules:
                    if rule[0] == self.field[j][i] and rule[2].match(area):
                        newfield[j][i] = rule[1]
                        break
        self.field = newfield

    def FastForward(self, n):
        for i in range(0, n):
            self.Step()

    def ReadRules(self, textstream):
        self.rules = []
        for line in textstream:
            words = line.split()
            self.rules += [(words[0], words[1], re.compile(' '.join(words[2:])))]

    def ReadState(self, textstream):
        self.field = []
        for line in textstream:
            self.field += [[]]
            for symbol in line.strip():
                self.field[-1] += symbol

    def WriteState(self, textstream):
        textstream.write(str(self))
    
    def __str__(self):
        string = ""
        for row in self.field:
            for state in row:
                string += str(state)
            string += '\n'
        return string.strip()
