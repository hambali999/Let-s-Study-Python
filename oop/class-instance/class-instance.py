#PART 1 - Class & Instances

print("Start Program ... ")
print("-------------------")


class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Cindy", 24)
student2 = Student("Alice", 23)
student3 = Student("Elon", 40)
         

print(student1.name, student1.age)
print(student2.name, student2.age)
print(student3.name, student3.age)