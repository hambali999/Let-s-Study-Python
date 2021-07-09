import json
import math


class Point():
    def __init__(self, x = 0, y = 0): #initialise x and y to 0
        self.__x = x
        self.__y = y

    #getter
    @property
    def x(self): return self.__x

    @property
    def y(self): return self.__y

    #setter
    @x.setter
    def x(self, newValue): self.__x = newValue

    @y.setter
    def y(self, newValue): self.__y = newValue

    #methods
    def move(self, dx, dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy

    def distanceTo(self, aPoint):
        return math.sqrt(math.pow((self.__x - aPoint.x), 2) + math.pow(self.__y - aPoint.y, 2))

    def quadrant(self):
        x = self.__x
        y = self.__y
        
        if x == 0 and y == 0: 
            return 0
        elif x > 0 and y > 0:
            return 1
        elif x < 0 and y < 0:
            return 3
        elif x < 0 and y > 0:
            return 4
        else: 
            return 2

    def __str__(self):
        return (self.__x, self.__y)


#code starts
point1 = Point()

print(point1.x)

point1.x = 20

print(point1.x)

point1.move(10,10)

print(point1.x, point1.y)

print(point1.__str__())

print(point1.quadrant())