class BankAccount:
    __defaultBalance = 100

    def __init__(self, accountId, pin, balance=__defaultBalance):
        self._accountId = accountId
        self._pin = pin
        self._balance = float(balance)

    #getter
    @property
    def accountId(self):
        return self._accountId

    @property
    def pin(self):
        return self._pin

    @property
    def balance(self):
        return self._balance

    #getter
    @pin.setter
    def pin(self, pin):
        self._pin = pin

    @balance.setter
    def balance(self, balance):
        self._balance = float(balance)

    #method
    def changePin(self, oldPin, newPin):
        if oldPin == self._pin:
            self._pin = newPin
            return True
        return False

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def transfer(self, anotherAccount, amount):
        if self.withdraw(amount):
            anotherAccount.deposit(amount)
            return True
        return False

    def __str__(self):
        return f'AccountID: {self._accountId} Balance: ${self._balance:,.2f}'


class Bank:
    def __init__(self, name) :
        self._name = name
        self._accounts = {}

    #getter
    @property
    def name(self): return self._name

    #methods
    def add(self, account):
        self._accounts[account.accountId].append(account) #append to dictionary 

    def search(self, accountId):
        if accountId in self._accounts:
            return self._accounts[accountId] #accountId is the key in the dict, returns the object in dict
        return None

    def remove(self, accountId):
        if accountId in self._accounts:
            del self._accounts[accountId]

    def transfer(self, accountId1, accountId2, amount):
        account1 = self.search(accountId1)
        account2 = self.search(accountId2)
        if account1 and account2 is not None:
            return account1.transfer(account2, amount)
        return False
    
    def listAll(self):
        print(f'Name: {self.name}')
        for accountId, account in self._accounts.items():
            print(f'Account: {account}')

def main():
    pass
