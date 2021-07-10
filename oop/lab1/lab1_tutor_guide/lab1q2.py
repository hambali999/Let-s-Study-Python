class Rectangle():
    def __init__(self, length, width):
        self._length = length 
        self._width = width 
    
    @property 
    def length(self):
        return self._length 
    
    @length.setter 
    def length(self, newLength):
        self._length = newLength 
    
    #repeat the same for width 

    def getArea(self):
        return self._length * self._width
    
    def getPerimeter(self):
        return (self._length + self._width) * 2
    
    def increaseSize(self, deltaL , deltaW):
        self._length += deltaL 
        self._width += deltaW
    
    def isBigger(self, r):
        # if self.getArea() > r.getArea():
        #     return True 
        # return False 

        return self.getArea() > r.getArea() #preferred way

    def __str__(self):
        return f'Length: {self._length} Width: {self._width} Area: {self.getArea()} Perimeter: {self.getPerimeter()}'

def test():
    r1 = Rectangle(10, 5)
    print( r1 )

test()