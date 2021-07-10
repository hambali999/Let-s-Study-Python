from datetime import datetime


class Flight:
    def __init__(self, flightNo, destination, departureDate):
        self._flightNo = flightNo
        self._destination = destination
        self._departureDate = departureDate

    @property
    def flightNo(self):
        return self._flightNo

    @property
    def destination(self):
        return self._destination

    @property
    def departureDate(self):
        return self._departureDate

    @flightNo.setter
    def flightNo(self, flightNo):
        self._flightNo = flightNo

    @departureDate.setter
    def departureDate(self, departureDate):
        self._departureDate = departureDate

    def __str__(self):
        return '{} {} {:%#d %b %Y %H:%M}'.format(self._flightNo, self._destination, self.departureDate)


class Passenger:
    def __init__(self, name, flight=None):
        self._name = name
        self._flight = flight

    def changeFlight(self, flight):
        self._flight = flight

    def __str__(self):
        return f'Name: {self._name} flight: {self._flight}'


def q1():
    flight = Flight('SQ1', 'LA', datetime(2019, 3, 30, 4, 15))
    p1 = Passenger('p1', flight)
    p2 = Passenger('p2', flight)
    print(p1)
    print(p2)
    flight.departureDate = datetime(2019, 3, 29, 15, 25)
    print(p1)
    print(p2)
    print(flight)


class BankAccount:
    __defaultBalance = 100

    def __init__(self, accountId, pin, balance=__defaultBalance):
        self._accountId = accountId
        self._pin = pin
        self._balance = float(balance)

    @property
    def accountId(self):
        return self._accountId

    @property
    def pin(self):
        return self._pin

    @property
    def balance(self):
        return self._balance

    @pin.setter
    def pin(self, pin):
        self._pin = pin

    @balance.setter
    def balance(self, balance):
        self._balance = float(balance)

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
    def __init__(self, name):
        self._name = name
        self._accounts = {}

    @property
    def name(self):
        return self._name

    def add(self, account):
        self._accounts[account.accountId] = account

    def search(self, accountId):
        if accountId in self._accounts:
            return self._accounts[accountId]

    def remove(self, accountId):
        acc = self.search(accountId)
        if acc is not None:
            self._accounts.pop(acc.accountId)
            # del self._accounts[acc] ## Alternative
            return True
        return False

    def transfer(self, accountId1, accountId2, amount):
        account1 = self.search(accountId1)
        account2 = self.search(accountId2)
        if account1 is not None and account2 is not None:
            return account1.transfer(account2, amount)
        return False

    def listAll(self):
        print(f'Name: {self.name}')
        for accountId, account in self._accounts.items():
            print(f'Account: {account}')


def getOption():
    options = [
        '1. Open bank account',
        '2. Check balance',
        '3. Transfer money',
        '4. Close account',
        '5. List all accounts',
        '0. Exit'
    ]

    for option in options:
        print(option)

    while True:
        opt = input('\nChoose your operation: ').strip()
        if opt in ''.join([str(i) for i in range(len(options))]):
            return int(opt)
        print('Invalid Input. Try again')


def addBankAccount(bank):
    accountId = input('Enter Account ID: ')
    pin = input('Enter PIN: ')
    balance = input('Enter Balance: ')
    added = bank.add(BankAccount(accountId, pin, balance))
    if added:
        print(f'{accountId} added')
    else:
        print(f'Account, {accountId}, already exist')


def checkBalance(bank):
    accountId = input('Enter Account ID: ')
    pin = input('Enter PIN: ')
    account = bank.search(accountId)
    if account is not None and account.pin == pin:
        print(account)
    else:
        print('Invalid entry.')


def transferMoney(bank):
    fromAcc = bank.search(input('Enter from Account ID: '))
    toAcc = bank.search(input('Enter to Account ID: '))
    amount = float(input('Enter to amount: $'))
    if fromAcc is not None and toAcc is not None:
        if fromAcc.transfer(toAcc, amount):
            print(f'${amount:,.2f} transferred from {fromAcc.accountId} to {toAcc.accountId}')
        else:
            print('Unable to transfer')
    else:
        print('Account(s) is not valid')


def closeAccount(bank):
    accountId = input('Enter Account ID: ')
    if bank.remove(accountId):
        print(f'{accountId} removed successfully')
    else:
        print(f'Failed to remove {accountId}')


def q2():
    bank = Bank('ABC')
    while True:
        opt = getOption()

        if opt == 1:
            addBankAccount(bank)

        elif opt == 2:
            checkBalance(bank)

        elif opt == 3:
            transferMoney(bank)

        elif opt == 4:
            closeAccount(bank)

        elif opt == 5:
            bank.listAll()

        else:
            break

        print()


class Product:
    def __init__(self, productCode, description, unitPrice):
        self._productCode = productCode
        self._description = description
        self._unitPrice = unitPrice

    @property
    def productCode(self):
        return self._productCode

    @productCode.setter
    def productCode(self, productCode):
        self._productCode = productCode

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def unitPrice(self):
        return self._unitPrice

    @unitPrice.setter
    def unitPrice(self, unitPrice):
        self._unitPrice = unitPrice

    def __str__(self):
        return f'productCode: {self._productCode}, description: {self._description}, unitPrice: ${self._unitPrice:,.2f}'


class CartItem:
    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity

    @property
    def cost(self):
        return self.product.unitPrice * self.quantity

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    def __str__(self):
        return f'quantity: {self._quantity}, cost: ${self.cost:,.2f}, product: {self._product}'


class ShoppingCart:
    def __init__(self, name):
        self._name = name
        self._items = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    def add(self, product):
        for item in self._items:
            if item.product == product:
                item.quantity += 1
                return
        self._items.append(product)

    def removeProduct(self, productCode):
        cartItem = self.search(productCode)
        if cartItem is not None:
            self.items.remove(cartItem)

    def search(self, productCode):
        for item in self.items:
            if item.product.productCode == productCode:
                return item

    def calculateTotalCost(self):
        total = 0
        for item in self.items:
            total += item.cost
        return total

    def __str__(self):
        return f"name: {self._name}, items: [{', '.join([f'Product: {item.product.description}, quantity: {item.quantity}' for item in self._items])}]"


def q3():
    shoppingCart = ShoppingCart('John Doe')
    p1 = Product('111', 'Apple', 1)
    p2 = Product('222', 'Orange', 2)
    p3 = Product('333', 'Pear', 3)
    cartItem1 = CartItem(p1, 2)
    cartItem2 = CartItem(p2, 3)
    cartItem3 = CartItem(p3, 4)
    shoppingCart.add(cartItem1)
    shoppingCart.add(cartItem2)
    shoppingCart.add(cartItem3)

    print(f"Search: {shoppingCart.search('111')}")
    print(f'Total Cost: ${shoppingCart.calculateTotalCost():,.2f}')

    print(shoppingCart)
    shoppingCart.removeProduct('111')
    print(shoppingCart)


class Employee:
    def __init__(self, id, name, hourlyRate):
        self._id = id
        self._name = name
        self._hourlyRate = hourlyRate

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def hourlyRate(self):
        return self._hourlyRate

    @hourlyRate.setter
    def hourlyRate(self, hourlyRate):
        self._hourlyRate = hourlyRate

    def __str__(self):
        return f'id: {self._id}, name: {self._name}, hourlyRate: {self._hourlyRate},'


class Company:
    def __init__(self, name, employees=[]):
        self._name = name
        self._employees = {}
        self._hourWorked = {}

        for employee in employees:
            self._employees[employee.id] = employee

    def recordHoursWorked(self, id, hour):
        if id in self._employees and id not in self._hourWorked:
            self._hourWorked[id] = float(hour)
            print(f'Hours worked recorded for employee {id}')
        elif id not in self._employees:
            print(f'Employee, {id}, does not exist')
        else:
            print(f'Employee {id} has existing work hours recorded')

    def deleteHoursWorked(self, id):
        if id in self._employees and id in self._hourWorked:
            self._hourWorked.pop(id)
            print(f'Hours worked for employee {id} has been removed')
        elif id not in self._employees:
            print(f'Employee {id} does not exist')
        else:
            print(f'Employee {id} do not have any work hours recorded')

    def getPay(self, id):
        if id in self._employees and id in self._hourWorked:
            return self._employees[id].hourlyRate * self._hourWorked[id]
        elif id not in self._employees:
            print(f'Employee {id} does not exist')
        else:
            print(f'Employee {id} do not have any recorded worked hours')


def getOption():
    options = [
        '1. Record hours worked',
        '2. Remove hours worked',
        '3. Get pay',
        '4. Quit'
    ]

    for option in options:
        print(option)

    while True:
        opt = input('\nChoose your operation: ').strip()
        if opt in ''.join([str(i) for i in range(1, len(options) + 1)]):
            return int(opt)
        print('Invalid Input. Try again')


def q4():
    e1 = Employee('E1', 'Adam', 1)
    e2 = Employee('E2', 'Ben', 2)
    e3 = Employee('E3', 'Cindy', 3)
    e4 = Employee('E4', 'David', 4)
    company = Company('ABC', [e1, e2, e3, e4])
    while True:
        opt = getOption()

        if opt == 4:
            break
        else:
            id = input('Enter employee ID: ')

            if opt == 1:
                company.recordHoursWorked(id, input('Enter workhours: '))
            elif opt == 2:
                company.deleteHoursWorked(id)
            else:
                salary = company.getPay(id)
                if salary is not None:
                    print(f'Salary for employee {id} is ${salary:,.2f}')
        print()


if __name__ == '__main__':
    q1()
    # q2()
    # q3()
    # q4()
