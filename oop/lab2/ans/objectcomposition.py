from cashcard import CashCard


class Customer:
    def __init__(self, name, cashcard):
        self._name = name
        self._cashcard = cashcard

    @property
    def name(self):
        return self._name

    @property
    def CardCard(self):
        return self._cashcard

    def topUp(self, amount):
        self._cashcard.topUp(amount)

    def __str__(self):
        return f'Name: {self._name} CashCard: {self._cashcard}'


def test():
    cc1 = CashCard(100)
    c1 = Customer('John', cc1)
    c1.topUp(50)
    print(c1)

    pass


if __name__ == '__main__':
    test()
