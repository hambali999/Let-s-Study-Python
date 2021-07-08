import json
import math

class Name():
    def __init__(self, gender, lastName, firstName, middleName):
        self.__gender = gender
        self.__lastName = lastName
        self.__firstName = firstName
        self.__middleName = middleName

    #GETTER METHODS
    @property
    def lastName(self): return self.__lastName

    @property
    def firstName(self): return self.__firstName

    @property
    def middleName(self): return self.__middleName

    #SETTER METHODS
    @lastName.setter
    def lastName(self, newLastName): self.__lastName = newLastName

    @firstName.setter
    def firstName(self, newFirstName): self.__firstName = newFirstName

    @middleName.setter
    def middleName(self, newMiddleName): self.__middleName = newMiddleName

    #METHODS
    def getFullName(self):
        salutation = 'Mr.' if self.__gender.lower() == 'm' else 'Ms.'
        return f'{salutation} {self.__lastName} {self.__firstName} {self.__middleName}'


    def getInitials(self):
        return f'{self.__firstName[0]}. {self.__middleName[0]}. {self.__lastName}'

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
        

student1 = Name('m', 'Ong', 'Ah', 'Kow')

# print(student1.lastName)

# student1.lastName = 'santa'

# print(student1.lastName)

print(student1.getFullName())

print(student1.getInitials())

print(student1.__str__())
