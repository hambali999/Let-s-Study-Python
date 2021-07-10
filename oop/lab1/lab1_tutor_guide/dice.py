import random 
class Dice():
    def __init__(self):
        self._value = 1

    @property 
    def value(self):
        return self._value
    
    def roll(self):
        self._value = random.randrange(1, 7)




d = Dice() 
print(d.value)
d.roll() 
print(d.value)