

class Name():
    def __init__(self, gender, lastName, firstName, middleName):
        self.__gender = gender
        self.__lastName = lastName
        self.__firstName = firstName
        self.__middleName = middleName

    #GETTER METHODS
    @property
    def lastName(self): return self.lastName

    @property
    def firstName(self): return self.firstName

    @property
    def middleName(self): return self.middleName

    # #SETTER METHODS
    # @lastName.setter
    # def lastName(self, newLastName): self.lastName = newLastName

    # @firstName.setter
    # def firstName(self, newFirstName): self.firstName = newFirstName

    # @middleName.setter
    # def middleName(self, newMiddleName): self.middleName = newMiddleName

    #METHODS
    def getFullName(self):
        salutation = 'Mr.' if self.gender.lower() == 'm' else 'Ms.'
        return f'{salutation} {self.lastName} {self.middleName} {self.firstName}'


    # def getInitials(self):
    #     return (self.first_name[0].upper()) + '.' + ' ' + (self.middle_name[0].upper()) + '.' + ' ' + (self.last_name) + '.'

        

student1 = Name('m', 'Last', 'first', 'middle')

print(student1.lastName)