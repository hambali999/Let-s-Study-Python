print("Start Program ... ")
print("-------------------")


class Student():

    #class attribute
    code = "student code"

    def __init__(self, name, age):

        #instance attribute
        self.name = name
        self.age = age


student1 = Student("Cindy", 24)
student2 = Student("Alice", 23)
student3 = Student("Elon", 40)
         

print(student1.name, student1.age)
print(student2.name, student2.age)
print(student3.name, student3.age)
print(student1.code)

print(f"My name is {student1.name} and i am {student1.age}")
print(f"My name is {student2.name} and i am {student2.age}")
print(f"My name is {student3.name} and i am {student3.age}")