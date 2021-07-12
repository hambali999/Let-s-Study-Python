class CashCard:
    _autoId = 1

    def __init__(self, amount):
        self._id = CashCard._autoId
        CashCard._autoId += 1
        self._amount = float(amount)

    @property
    def id(self):
        return self._id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    def topUp(self, amount):
        self._amount += amount

    def deduct(self, amount):
        if self._amount >= amount:
            self._amount -= amount
            return True
        return False

    def __str__(self):
        return f'ID: {self._id}, Amount: ${self._amount:,.2f}'
