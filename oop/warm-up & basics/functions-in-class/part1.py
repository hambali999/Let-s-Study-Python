print("Start Program ... ")
print("-------------------")


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


# Initializing the objects
student1 = Student("Cindy", 24)
student2 = Student("Alice", 23)
student3 = Student("Elon", 40)

# Print
print(student1.base_salary())
print(student2.base_salary())
print(student3.base_salary())

print(student3.old())


print(f"My name is {student1.name} and i am {student1.age}, I have a base salary of ${student1.base_salary()}")
print(f"My name is {student2.name} and i am {student2.age}, I have a base salary of ${student2.base_salary()}")
print(f"My name is {student3.name} and i am {student3.age}, I have a base salary of ${student3.base_salary()}")

print(f"Oh btw I am {student1.name} and {student1.old()}")
print(f"Oh btw I am {student2.name} and {student2.old()}")
print(f"Oh btw I am {student3.name} and {student3.old()}")


