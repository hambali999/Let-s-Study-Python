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



p1 = Phone('123')
p1.assignSpeedDial(1, 123)
p1.speedDial(0)
p1.speedDial(1)
p1.displayAllSpeedDial()