print("Start Program ... ")
print("-------------------")

#parent
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def base_salary(self):
        if self.age < 20:
            return 1500
        elif self.age < 30:
            return 4000
        else: 
            return 10000

    def old(self):
        if self.age >= 40:
            return 'IM QUITE OLD EH LOLL'
        else:
            return 'IM STILL YOUNG HELLO'

class SoftwareEngineer(Student):
    def __init__(self, name, age, major):
        super().__init__(name, age)              #DONT PUT SELF
        self.major = major

class Designer(Student):
    def __init__(self, name, age, major):
        super().__init__(name, age)             #DONT PUT SELF
        self.major = major


# Initializing the objects
student1 = SoftwareEngineer("Cindy", 24, 'SE')
student2 = Student("Alice", 23)
student3 = Student("Elon", 40)

# Print
print(student1.major)

