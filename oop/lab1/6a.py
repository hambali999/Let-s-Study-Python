

class ToDo():
    def __init__(self, event):
        self.__event = event
        self.__eventList = []

    #getter
    @property
    def event(self): return self.__event

    #methods
    def addToDo(self, toDo):
        self.__eventList.append(toDo)

    def displayToDoList(self):
        print(f"Event: {self.__event}")
        for idx, val in enumerate(self.__eventList):
            print(f"{idx}. {val}")

    def deleteToDoItem(self, index):
        for idx, val in enumerate(self.__eventList):
            if idx == index:
                # print(val)
                self.__eventList.pop(idx)

toDo = ToDo('Things to bring tomorrow')
toDo.addToDo('Bring passport')
toDo.addToDo('Change money')
toDo.addToDo('Bring medicine')
toDo.displayToDoList()
toDo.deleteToDoItem(2)
toDo.displayToDoList()


