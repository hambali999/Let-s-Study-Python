import json
import math

#length - float
#width - float 

class Rectangle():
    def __init__(self, length, width):
        self.__width = width
        self.__length = length

    #GETTER
    @property
    def width(self): return self.__width

    @property
    def length(self): return self.__length

    #SETTER
    @width.setter
    def width(self, newWidth): self.__width = newWidth

    @length.setter
    def length(self, newLength): self.__length = newLength

    #METHODS
    def getArea(self):
        area = self.__width * self.__length
        return (area)

    def getPerimeter(self):
        perimeter = (self.__width * 2) + (self.__length * 2)
        return (perimeter)

    def increaseSize(self, length, width):
        self.__length = length
        self.__width = width
        print(f'new width is {self.__width} and new length is {self.__length}')

    def isBigger(self, r):
        currentArea = self.__width * self.__length
        if currentArea > r:
            return True
        else: 
            return False

    # def __str__(self):
    # return json.dumps(self, default=lambda o : o.__dict__, indent=4)
    def __str__(self):
        return f'Length: {self.__length} Width: {self.__width} Area: {self.getArea()}'



#CODING STARTS ~
shape1 = Rectangle(10,20)

print(shape1.length, shape1.width)

shape1.length = 50

print(shape1.length, shape1.width)

print(shape1.getArea())

print(shape1.getPerimeter())

shape1.increaseSize(10, 10)

print(shape1.isBigger(20)) #TRUE

print(shape1.isBigger(200)) #FALSE

print(shape1.__str__())











