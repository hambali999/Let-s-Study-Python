import random

class MemoryGame(): 
    def __init__(self, size):
        self._cards =[]
        self._size = size
        self._guess = [''] * (size * size)
        letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        while True:
            aletter = letters.pop(random.randrange(len(letters))) #extract a letter from list 
            self._cards += list(aletter * 2) #even those odd size will be filled up with a letter
            if len(self._cards) >= size*size:
                break     
        if size%2==1:
            temp = self._cards[:-2] #extract up to the second last to shuffle
            random.shuffle(temp)
            self._cards =temp + ['NIL'] #add a NIL
        else:
            random.shuffle(self._cards)
    
    def displayGrid(self, cheat=False):
        if cheat:
            cards = self._cards[:]
        else:
            cards = self._guess[:]
        print('    Columns')
        temp='Rows' + '| ' + ' | '.join( str(n) for n in range(1, self._size+1)) + ' |'
        dots='    ' + '-' * (len(temp) -4)
        print(temp)
        cds = [ f'{c:^3}' for c in cards ]
        for n in range(self._size):
            print(f'{dots:>s}')
            print(f'{str(n+1):>4s}|'+ '|'.join(cds[n*self._size : self._size*(n+1)]) +'|')
        print(f'{dots:>s}')
    
    def getCard(self, row, col):
        return self._cards[self._size * (row-1) + col-1]

    def setGuess(self, row, col, letter):
        self._guess[self._size * (row-1) + col-1] = letter

    def isGameOver(self):
        return all( [self._cards[n]==self._guess[n] for n in range(len(self._cards)) ])

def test():
    mg = MemoryGame(4)
    mg.displayGrid(cheat=True)
    mg.displayGrid()
    mg.setGuess(1,1,'A')
    print( mg.isGameOver() )

if __name__ == '__main__':
    test()
