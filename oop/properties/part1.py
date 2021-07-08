#PROPERTIES - MORE PYTHONIC WAY LOL

class Student():
    def __init__(self, name):
        self._name = name

    #getter
    @property
    def name(self): 
        return self._name

    #setter
    @name.setter
    def name(self, value): 
        self._name = value



student1 = Student("bali")

print(student1.name)


 #why do we it do we this way? : this should applies it in encapsulation principle

 #getter and setter method which is the only way we can access it from the outside
