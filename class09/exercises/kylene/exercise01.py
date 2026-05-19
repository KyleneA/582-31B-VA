# Exercise 01
class Student:
    def __init__(self, name, gpa):
        if (0.0 <= gpa <= 4.0):
            self.name = name
            self.__gpa = gpa
        else:
            print("Please enter valid GPA")
    
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, new_gpa):
        if (0.0 <= new_gpa <= 4.0):
            self.__gpa = new_gpa
        else:
            print("Please enter valid GPA")

student = Student("Bob", 3.6)
print("Bob: ", student.gpa)
student.gpa = 4.0
print("Bob: ", student.gpa)