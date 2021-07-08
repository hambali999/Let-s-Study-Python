import json
import math


class Name:
    def __init__(self, gender, lastName, firstName, middleName):
        self.__gender = gender
        self.__lastName = lastName
        self.__firstName = firstName
        self.__middleName = middleName

    @property
    def lastName(self):
        return self.__lastName

    @property
    def firstName(self):
        return self.__firstName

    @property
    def middleName(self):
        return self.__middleName

    @lastName.setter
    def lastName(self, lastName):
        self.__lastName = lastName

    @firstName.setter
    def firstName(self, firstName):
        self.__firstName = firstName

    @middleName.setter
    def middleName(self, middleName):
        self.__middleName = middleName

    def getFullName(self):
        salutation = 'Mr.' if self.__gender.lower() == 'm' else 'Ms.'
        return f'{salutation} {self.__lastName} {self.__firstName} {self.__middleName}'

    def getInitials(self):
        return f'{self.__firstName[0].upper()}. {self.__middleName[0].upper()}. {self.__lastName}'

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


def q1():
    name = Name('M', 'Lai', 'Kai', 'Ying')
    print(name)

    print(name.getFullName())
    print(name.getInitials())

    print('firstName')
    print(name.firstName)
    name.firstName = '0'
    print(name.firstName)

    print('lastName')
    print(name.lastName)
    name.lastName = '1'
    print(name.lastName)

    print('middleName')
    print(name.middleName)
    name.middleName = '2'
    print(name.middleName)

    print(name)


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.width

    @length.setter
    def length(self, length):
        self.__length = length

    @width.setter
    def width(self, width):
        self.__width = width

    def getArea(self):
        return self.__length * self.__width

    def getPerimeter(self):
        return (self.length + self.__width) * 2

    def increaseSize(self, length, width):
        self.__length += length
        self.__width += width

    def isBigger(self, r):
        return self.getArea() > r.getArea()

    # def __str__(self):
    #     return json.dumps(self, default=lambda o : o.__dict__, indent=4)
    def __str__(self):
        return f'Length: {self.__length} Width: {self.__width} Area: {self.getArea()}'


def q2():
    rectangle = Rectangle(2, 3)
    print(rectangle)

    rectangle.length = 4
    rectangle.width = 5
    print(rectangle)

    print(rectangle.getArea())
    print(rectangle.getPerimeter())

    rectangle.increaseSize(2, 3)
    print(rectangle)
    print('IsBigger: ', rectangle.isBigger(20))
    print('IsBigger: ', rectangle.isBigger(50))


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def distanceTo(self, aPoint):
        return math.sqrt(math.pow((self.__x - aPoint.x), 2) + math.pow(self.__y - aPoint.y, 2))

    def quadrant(self):
        x = self.__x
        y = self.__y
        if x == 0 or y == 0:
            return 0
        elif x > 0 and y > 0:
            return 1
        elif x < 0 and y < 0:
            return 3
        elif x > 0:
            return 2
        else:
            return 4

    def __str__(self):
        return str((self.__x, self.__y))


def q3():
    point = Point(2, 3)
    print(point)
    print(point.x)
    print(point.y)

    point.x = 4
    point.y = 5
    print(point)

    point.move(1, 2)
    print(point)
    print('Quadrant:', point.quadrant())

    point.x = 1
    point.y = -1
    print('Quadrant:', point.quadrant())

    point.x = -1
    point.y = -1
    print('Quadrant:', point.quadrant())

    point.x = -1
    point.y = 1
    print('Quadrant:', point.quadrant())

    print('Question\'s test')
    p1 = Point(5, 1)
    print(p1)
    point.move(5, -5)
    p2 = Point(10, -10)
    print(p1.distanceTo(p2))
    print('p1 quadrant:', p1.quadrant())
    print('p2 quadrant:', p2.quadrant())


class BankAccount:
    __defaultBalance = 100

    def __init__(self, accountId, pin, balance=__defaultBalance):
        self.__accountId = accountId
        self.__pin = pin
        self.__balance = float(balance)

    @property
    def pin(self):
        return self.__pin

    @property
    def balance(self):
        return self.__balance

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @balance.setter
    def balance(self, balance):
        self.__balance = float(balance)

    def changePin(self, oldPin, newPin):
        if oldPin == self.__pin:
            self.__pin = newPin
            return True
        return False

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        return False

    def transfer(self, anotherAccount, amount):
        if self.withdraw(amount):
            anotherAccount.deposit(amount)
            return True
        return False

    def __str__(self):
        return f'accoundId: {self.__accountId} balance: ${self.__balance:,.2f}'


def q4():
    accounts = []
    acc1 = BankAccount('B1', 111)
    accounts.append(acc1)
    acc1.deposit(100)
    print(acc1)
    acc1.changePin(111, 222)
    acc2 = BankAccount('B2', 111)
    accounts.append(acc2)
    isSuccess = acc2.withdraw(200)
    print('acc2 withdrawal is successful:', isSuccess)
    isTransferSuccess = acc1.transfer(acc2, 100)
    print('acc1 transfer to acc2 is successful:', isTransferSuccess)
    if isTransferSuccess:
        print('acc1 balance:', acc1.balance)
        print('acc2 balance:', acc2.balance)
    for account in accounts:
        print(account)


class Phone:
    __notAssignHolder = 0

    def __init__(self, phone):
        self.__phone = phone
        self.__dialList = [type(self).__notAssignHolder] * 10

    @property
    def phone(self):
        return self.__phone

    def assignSpeedDial(self, digit, phone):
        if digit not in range(len(self.__dialList)):
            print('Invalid digit')
        else:
            self.__dialList[digit] = phone

    def speedDial(self, digit):
        if digit not in range(10):
            print('Invalid digit')
        else:
            number = self.__dialList[digit]
            if number == type(self).__notAssignHolder:
                print('No number assigned')
            else:
                print(f'calling {number}')

    def displayAllSpeedDial(self):
        print(f'My speed dial number: {self.__phone}')
        for i in range(len(self.__dialList)):
            print(f'{i} - {self.__dialList[i]}')

    def __str__(self):
        return str(self.__dialList)


def q5():
    p1 = Phone('123')
    p1.assignSpeedDial(1, 123)
    p1.speedDial(0)
    p1.speedDial(1)
    p1.displayAllSpeedDial()


class ToDo:
    def __init__(self, event):
        self.__event = event
        self.__eventList = []

    @property
    def event(self):
        return self.__event

    def addToDo(self, toDo):
        self.__eventList.append(toDo)

    # def displayToDoList(self):
    #     print(f'Event:{self.event}')
    #     for i in range(len(self.__eventList)):
    #         print(f'{i + 1}. {self.__eventList[i]}')

    def displayToDoList(self):
        print(f'Event:{self.event}')
        for i, item in enumerate(self.__eventList):
            print(f'{i + 1}. {item}')

    def deleteToDoItem(self, index):
        if len(self.__eventList) > index - 1:
            del self.__eventList[index - 1]


def q6():
    toDo = ToDo('Things to bring tomorrow')
    toDo.addToDo('Bring passport')
    toDo.addToDo('Change money')
    toDo.addToDo('Bring medicine')
    toDo.displayToDoList()
    toDo.deleteToDoItem(2)
    toDo.displayToDoList()


class FileAnalyzer:
    __contents = ''

    def __init__(self, fileName):
        with open(fileName, 'r') as file:
            type(self).__contents = file.read()
            file.close

    @classmethod
    def displayContents(cls):
        print(cls.__contents)

    @classmethod
    def numberOfWords(cls):
        return len(cls.__contents.split())

    @classmethod
    def displayWithLineNumber(cls):
        lines = cls.__contents.split('\n')
        for i in range(len(lines)):
            print(f'{i + 1} {lines[i]}')

    @classmethod
    def search(cls, word):
        lines = cls.__contents.split('\n')
        for i in range(len(lines)):
            if word.lower() in lines[i].lower():
                print(f'{i + 1} {lines[i]}')

    @classmethod
    def appendALine(cls, line):
        if cls.__contents[-2:] != '\n':
            cls.__contents += '\n'
        cls.__contents += (line + '\n')


def q7():
    fileAnalyzer = FileAnalyzer('lab_1.py')
    fileAnalyzer.displayContents()
    print(fileAnalyzer.numberOfWords())
    fileAnalyzer.displayWithLineNumber()
    word = input('Enter a search word: ')
    fileAnalyzer.search(word)
    fileAnalyzer.appendALine('This is a new line')
    fileAnalyzer.displayContents()


if __name__ == '__main__':
    # q1()
    # q2()
    # q3()
    q4()
    # q5()
    # q6()
    # q7()
