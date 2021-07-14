import random
def method1():
    diceCount = [0, 0, 0, 0, 0, 0, 0]
    throws = 100
    diceList = []

    for i in range(1, throws+1):
        randomThrow = (random.randrange(1,6+1))
        diceList.append(randomThrow)
    face1 = diceList.count(1)
    face2 = diceList.count(2)
    face3 = diceList.count(3)
    face4 = diceList.count(4)
    face5 = diceList.count(5)
    face6 = diceList.count(6)

    print("Dice\tOccurrence")
    print(f"1\t{face1}")
    print(f"2\t{face2}")
    print(f"3\t{face3}")
    print(f"4\t{face4}")
    print(f"5\t{face5}")
    print(f"6\t{face6}")

    print(len(diceList)) #just to make sure there are 100 throws


def method2():
    diceCount = [0, 0, 0, 0, 0, 0, 0]
    throws = 100
    diceList = []

    for i in range(1, throws+1):
        randomThrow = (random.randrange(1,6+1))
        diceList.append(randomThrow)
    for i in diceList:
        if i == 1:
            diceCount[1] += 1
        elif i == 2:
            diceCount[2] += 1
        elif i == 3:
            diceCount[3] += 1
        elif i == 4: 
            diceCount[4] += 1
        elif i == 5:
            diceCount[5] += 1
        elif i == 6:
            diceCount[6] += 1
        else:
            pass

    print(diceCount)

    print("Dice\tOccurrence")
    for i in range(7):
        print(f"{i}\t{diceCount[i]}")
    print(f"Total\t{sum(diceCount)}")
    # print(len(diceList)) #just to make sure there are 100 throws

def method3():
    
    #     this function simulates throwing of a dice, 100 times
    #     it keeps tracks of the number of occurences of each face value (1-6).
    #     it displays the number of occurences after 100 throws.

    diceCount = [0]*7 #type in pdf, not *6
    #loop 100times
    for i in range(100):
        num = random.randint(1,6)
    #generate a random value (1-6)
        diceCount[num]+=1
    #update diceCount (increment respective index by 1)

    #print summary
    print("Dices \tSummary")
    print(diceCount)
    #print dice values and occurrences
    for i in range(1,7):
        print(f"{i}\t{diceCount[i]}")
    print(f"Total\t{sum(diceCount)}")

method3()

#method3, BEST METHOD, CONCISE & SIMPLE, but takes time to understand