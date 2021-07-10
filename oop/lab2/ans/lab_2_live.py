class CashCard:
    _autoId = 1

    def __init__(self, amount):
        self._id = 'C' + str(CashCard._autoId)
        CashCard._autoId += 1
        self._amount = amount

    @property
    def id(self):
        return self._id

    @property
    def amount(self):
        return self._amount

    def topUp(self, amount):
        self._amount += amount


def q1():
    c1 = CashCard(100)
    print(c1.id)
    c2 = CashCard(200)
    print(c2.id)
    c1.topUp(50)
    # print(c1.amount)
    # print(c2.amount)


class PC:
    _printer = 'HP Laser printer'

    def __init__(self, brand):
        self._brand = brand

    @classmethod
    def getPrinter(cls):
        return cls._printer

    @classmethod
    def setPrinter(cls, printer):
        cls._printer = printer

    def printTo(self):
        print('Printing to', PC._printer)


def q2():
    pc1 = PC('Lenovo')
    pc2 = PC('Asus')
    pc1.printTo()
    pc2.printTo()
    print(pc1.getPrinter())
    pass


## Object Composition
## Object that is composed of other object

if __name__ == '__main__':
    q1()
    # q2()
