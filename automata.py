from abc import ABCMeta, abstractmethod, abstractproperty
from itertools import islice, cycle, chain
from copy import deepcopy
import io
import re


DEBUG = False


class CellularAutomata:
    def __init__(self):
        self.field = []
        self.rules = []

    def step(self):
        newfield = deepcopy(self.field)
        for j in range(0, len(self.field)):
            for i in range(0, len(self.field[j])):
                h = len(self.field)
                w = len(self.field[0])
                # Everything in this chain of transformations is basically
                # an iterator, therefore it's not as inefficient as it looks.
                #(still slow as hell)
                area = islice(cycle(self.field), h + j - 1, h + j + 2)
                area = (islice(cycle(row), w + i - 1, w + i + 2)
                        for row in area)
                area = chain.from_iterable(area)
                area = list(area)
                area = area[0:3] + area[5:6] + area[6:9][::-1] + area[3:4]
                area = ''.join(area)

                for rule in self.rules:
                    if rule[0] == self.field[j][i] and rule[2].match(area):
                        if DEBUG:
                            print(rule[0], " -> ", rule[1], " where ",
                                  area, " matched ", rule[2].pattern)
                        newfield[j][i] = rule[1]
                        break

        self.field = newfield

    def fast_forward(self, n):
        for i in range(0, n):
            self.step()

    def read_rules(self, textstream):
        self.rules = []
        for line in textstream:
            line = line.strip()
            self.rules += [(line[0], line[1], re.compile(line[2:]))]

        if DEBUG:
            print(self.rules)

    def read_state(self, textstream):
        self.field = []
        for line in textstream:
            self.field += [[]]
            for symbol in line.strip():
                self.field[-1] += symbol

    def write_state(self, textstream):
        textstream.write(str(self))

    def __str__(self):
        return '\n'.join(map(''.join, self.field))
