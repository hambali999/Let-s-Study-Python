#dice guessing game
import random 

d1 = random.randrange(1, 7)
print(d1)

##OO way using a dice
from dice import Dice 

d1 = Dice() # creates a dice object 
d1.roll() #give a random dice value 1-6
print(d1.value)

##Card game
##52 cards. each card Jack of Spade, Ace of Heart
#cards = [ ['Spade','Ace', 1], ['Heart','Jack', 11] ] #52 nested list

##OO way
from cards import * 

deck = Deck() # creates a deck of 52 cards
deck.shuffle() #shuffles 
c1 = deck.dealCard() #deal a card from the deck
print( c1 )

from memgame import * 

mg = MemoryGame(4)
mg.displayGrid(cheat=True)
mg.displayGrid()
mg.setGuess(1, 1, 'A')
mg.displayGrid()

