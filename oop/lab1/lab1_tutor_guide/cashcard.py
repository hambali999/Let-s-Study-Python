class CashCard(): #template/factory to create card
    #attributes
    def __init__(self, id, amount):
        #creating the attributes self._id and self._value
        self._id = id #attribute will have the self keyword infront. 
        self._value = amount #self is only used within a class.
                             #attribute names should have a underscore before the name. e.g. _id _value
                             #underscore means this attribute SHOULD NOT be accessed directly
        

    #property defines what value the user can access. Whether to read or write  
    @property 
    def id(self):
        return self._id
    @property  
    def value(self):    #read only
        return self._value
    @value.setter 
    def value(self, amount): #setter allows the attribute to be modified
        self._value = amount


    #methods/behaviour/actions
    def topUp(self, amt):
        self._value += amt
    
    def deduct(self, amt):
        if amt <= self._value:
            self._value -= amt
    
    #compare with another CashCard
    def hasMoreValue(self, anotherCard): #compare whether self has more value than the another card
        if self._value > anotherCard.value:
            return True 
        return False
     

    def __str__(self): #returns all the attribute values as a string
        return f'Id: {self._id} Value: ${self._value:.2f}'


def test():
    x = 10
    #create a CashCard object id of 'c1', initial amount 100 
    c1 = CashCard('c1', 100)
    c2 = CashCard('c2', 200)
    print( c1._value ) #accessing the value attribute. BUT NOT suppose to!!
    print( c1.value )
    #to modify the value of the cash card
    c1.value = 500 #provided there is a setter written in the class
    print( c1.id, c1.value)
    print( c1.__str__() )
    print( c1 ) #default will call c1.__str__() provided that has been defined.
    c1.topUp(100)
    print(c1)
    c1.deduct(5000)
    print(c1)
    print(c1.hasMoreValue(c2)) #does c1 have more value than c2?
    if c1.value > c2.value:
        print(c1, 'has more value')
    
    print(c1._value)
    #print(c1.__x) #is it really hidden??
   


if __name__=='__main__':
    test()