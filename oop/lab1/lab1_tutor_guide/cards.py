import random 
class Card():
    """
    Creates a card with a suit and value
    suit is Spade,Heart,Diamond,Club
    value is A,1,2,3,4,5,6,7,8,9,J,Q,K
    """
    def __init__(self, suit, value):
        self._suit = suit 
        self._value = value 
    
    @property 
    def suit(self):
        '''returns the suit'''
        return self._suit 
    @property 
    def value(self):
        """returns the value"""
        return self._value 
    def compareByValue(self, card):
        """
        compares 2 cards by value
        parameter: another card
        returns: -1 if smaller than card
        0 if same
        1 if higher in value'''
        values=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        if values.index(self.value) < values.index(card.value):
            return -1
        elif values.index(self.value) ==values.index(card.value):
            return 0
        else: 
            return 1
        """
    def compareTo(self, card):
        values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suit =['Club','Diamond','Heart','Spade']
        #Spade>Heart>Diamond>Club
        if suit.index(self._suit) == suit.index(card.suit):
            if values.index(self._value) < values.index(card._value):
                return -1
            elif  values.index(self._value) > values.index(card._value):
                return 1
            else: 
                return 0
        elif suit.index(self._suit) < suit.index(card.suit):
            return -1
        elif suit.index(self._suit) > suit.index(card.suit):
            return 1
             
            
    def __str__(self):
        return self._value + ' of ' +self._suit 

class Deck():
    def __init__(self):
        self.__cards = []
        suit =['Spade','Heart','Diamond','Club']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.__cards=[]
        for n in range(0, 4): #suit
            for m in range(0, 13):
                self.__cards.append(Card(suit[n],values[m]))
        
    def shuffle(self):
        random.shuffle(self.__cards)
        #for c in self.__cards:
        #    print(c)
            
    def dealCard(self):
        return self.__cards.pop()
    
    
    
def test():
    d = Deck()
    d.shuffle()
    c1 = d.dealCard()
    c2 = d.dealCard()
    c3 = d.dealCard()
    print(c1, c2, c3)

if __name__=='__main__':
    d = Deck()
    d.shuffle()
    c1 = d.dealCard()
    c2 = d.dealCard()
    print(c1)
    print(c2)
