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
        super().__init__(name, age) #DONT PUT SELF
        self.major = major

class Designer(Student):
    def __init__(self, name, age, major):
        super().__init__(name, age) #DONT PUT SELF
        self.major = major


# Initializing the objects
student1 = SoftwareEngineer("Cindy", 24, 'Programming')
student2 = Designer("Alice", 23, "Design")
student3 = Designer("Elon", 40, "Art")

# Print
# print(student1.major)

print(f"Hi my name is {student1.name} and my age is {student1.age}, I majored in {student1.major}")
print(f"Hi my name is {student2.name} and my age is {student2.age}, I majored in {student2.major}")
print(f"Hi my name is {student3.name} and my age is {student3.age}, I majored in {student3.major}")


