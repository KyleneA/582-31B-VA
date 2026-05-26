from studentLevel import StudentLevel

class Student:
    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, value):
        if not isinstance (value, StudentLevel):
            raise ValueError("Student's level must be a StudentValue value.")
        else:
            self.__level = value

    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def display_info(self):
        print(f"Name: {self.name} | Level: {self.level.value}")