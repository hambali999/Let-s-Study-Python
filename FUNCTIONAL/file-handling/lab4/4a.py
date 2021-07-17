

def main():
    nric = 'S7928964G'
    weight = (2, 7, 6, 5, 4, 3, 2)
    products = []
    nricNo = []
    Sum = 0
    remainder = 0
    digit = 0
    remainderList = []
    lastDigit = 0

    for i in nric[1:-1]:
        nricNo.append(int(i)) 

    for num1, num2 in zip(nricNo, weight):
    	products.append(num1 * num2)

    Sum = sum(products)
    remainder = round(Sum/11, 1)
    for i in str(remainder):
        remainderList.append(i)
    lastDigit = remainderList[-1]
    # print(lastDigit)

    digit = 11 - int(lastDigit)

    

    print(products)
    print(Sum)
    print(remainder)
    print(digit)


# Conversion: ABCDEFGHI Z J 
# Table 12 3 45 67 891011


import random
def checkNric():

    nric = input("Enter nric: ").upper()
    weight = (2,7,6,5,4,3,2)

    #step 1 and 2
    total = 0
    for i in range(1,8): #index 1 to 7 of nric
        total += int(nric[i])*weight[i-1]

    #step 3
    rem = total%11 #modular (remainder) division

    #step 4
    checkDigit = 11 - rem

    #step 5
    convTable = ("","A","B","C","D","E","F","G","H","I","Z","J")
    if nric[8]==convTable[checkDigit]:
        print("nric is valid")
    else:
        print("nric is not valid")

checkNric()