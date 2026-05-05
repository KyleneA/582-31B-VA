# instance methods vs class methods !
class Student:
    school_name = "ABC College"

    def __init__(self, name):
        self.name = name

    # instance method!
    # here introduce belongs to an instance of class Student
    def introduce(self):
        print(f"My name is {self.name}")

student1 = Student("John Doe")
student2 = Student("Jane Doe")

# introduce here only works with one object 
student1.introduce()
student2.introduce()

# Sometimes, we might need a method that changes a class attribute!

# we might also need a helper method that checks if everything is valid !

# from here we move towards class methods and static methods.

# Instance methods, take self and they work with one object!


# if we go towards a class method:
    # class method works with the class itself
    # it receives cls instead of self (as signature)
    # it's also marked with @classmethod

class Student:
    school_name = "ABC College"

    def __init__(self, name):
        self.name = name

    @classmethod # we add the mark
    def show_school(cls): # cls as signature
        print(f"School: {cls.school_name}") #cls instead of self

Student.show_school()