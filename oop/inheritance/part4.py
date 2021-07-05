print("START PROGRAM ... ")
print("----------------")


class Student():
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

class SoftwareEngineer(Student): #PLEASE REMEMBER TO TAKE IN THE PARENT CLASS 'Student' INSIDE THIS CLASS FFS
    def __init__(self, name, age, school, role):
        super().__init__(name, age, school)
        self.role = role

class Artist(Student):
    def __init__(self, name, age, school, role):
        super().__init__(name, age, school)
        self.role = role

student1 = SoftwareEngineer("John", 21, "Computer School", 'Software Engineer')
student2 = Artist("Jake", 25, "Art School", 'Artist')

print(f"Whats up peeps, my name is {student1.name} and i am {student1.age}. I am currently attending {student1.school} as a {student1.role}")
        
