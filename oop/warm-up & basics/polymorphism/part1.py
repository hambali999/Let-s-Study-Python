#POLYMORPHISM

print("START PROGRAM ... ")
print("----------------")

class Student():
    def __init__(self, name, age, school, role):
        self.name = name
        self.age = age
        self.school = school
        self.role = role

    def work(self):
        print("I am working as a normal student!")

class SoftwareEngineer(Student): #PLEASE REMEMBER TO TAKE IN THE PARENT CLASS 'Student' INSIDE THIS CLASS FFS
    def __init__(self, name, age, school, role, level):
        super().__init__(name, age, school, role)
        self.role = role
        self.level = level
    
    def work(self):
        print(f"I am working as a {self.role}")

class Artist(Student):
    def __init__(self, name, age, school, role, level):
        super().__init__(name, age, school, role)
        self.role = role
        self.level = level

    def work(self):
        print(f"I am working as an {self.role}")

student1 = SoftwareEngineer("John", 21, "Computer School", 'Software Engineer', 2)
student2 = Artist("Jake", 25, "Art School", 'Artist', 3)
student3 = Student("Alice", 25, "Art School", "Student")

# print(f"Whats up peeps, my name is {student1.name} and i am {student1.age}. I am currently attending {student1.school} as a {student1.role}")
        
# print(f"Whats up peeps, my name is {student2.name} and i am {student2.age}. I am currently attending {student2.school} as a {student2.role}")

# print(f"Whats up peeps, my name is {student3.name} and i am {student3.age}. I am currently attending {student3.school} as a {student3.role}")

# student1.work()
# student2.work()
# student3.work()

#POLYMORPHISM
students = [
    SoftwareEngineer("John", 21, "Computer School", 'Software Engineer', 2),
    Artist("Jake", 25, "Art School", 'Artist', 3),
    Student("Alice", 25, "Art School", "Student")
]


def motivate_student(students):
    for student in students:
        student.work()

motivate_student(students)