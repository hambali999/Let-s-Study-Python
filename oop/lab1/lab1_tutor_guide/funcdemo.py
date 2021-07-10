#passing optional parameters to functions.

def printPattern(symbol, row=1, col=1): #default row is 1, col is 1
    for n in range(row): 
        print( symbol * col)
    
def dummy():
    print('dummy function')


def test():
    #printPattern('*', 2, 5)
    printPattern('@', 1, 10)
    printPattern('*')  #row will be 1, col also 1
    printPattern('#', 5) #5 rows, use the default 1 col
    printPattern('$', col=5) #use the default row value, col to be 5
    printPattern(symbol='%', row=2, col=10)


#print( __name__ ) #2 underscore before and after (2 underscores is called dundar) Internal name
                  # if you run from THIS module, the name is __main__

if __name__ == '__main__': #if running within this module, then call the test function.
    test()
