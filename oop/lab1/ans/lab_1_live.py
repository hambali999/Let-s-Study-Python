import random

import lab_1


def printPattern(symbol, row=1, col=1):
    for n in range(row):
        print(symbol * col)


## Validate that it's executing from this file itself
if __name__ == '__main__':
    lab_1.q1()
    printPattern('*', col=5, row=3)


class Dice():
    def __init__(self):
        self._value = 1

    @property
    def value(self):
        return self._value

    def roll(self):
        self._value = random.randint(1, 6)


d = Dice()
print(d.value)
d.roll()
print(d.value)
