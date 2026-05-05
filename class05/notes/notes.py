# instance vs class methods
class Student:
    school_name = "ABC College"

    def __init__(self, name):
        self.name = name

    # instance method
    def introduce(self):
        print(f"my name is {name}")

student1 = Student("John Doe")