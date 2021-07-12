class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def substract(self):
        return self.x - self.y

class Math2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

class Math3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.m1 = Math(x,y)
        self.m2 = Math2(x,y)

    def power(self):
        return self.x ** self.y

    def add(self):
        return self.m1.add()

    def substract(self):
        return self.m1.substract()

    def multiply(self):
        return self.m2.multiply()

m1 = Math3(8, 3)
# m2 = Math3(1, 2)
print (f"add", m1.add())
print (f"multiply", m1.multiply())
print (f"substract", m1.substract())
print (f"power", m1.power())

