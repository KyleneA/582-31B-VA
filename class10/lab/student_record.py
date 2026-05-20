class StudentRecord:
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if ((0.0 > value) or (value > 4.0)):
            print("Student GPA must be between 0.0 and 4.0")
        else:
            self.__gpa = value
    
    @property
    def credits(self):
        return self.__credits
    
    @credits.setter
    def credits(self, value):
        if (value <= 0):
            print("Student credits must be greater or equal to 0")
        else:
            self.__credits = value

    def __init__(self, name, gpa, credits):
        if (len(name) == 0 ):
            print("Student name cannot be empty")
        else:
            self.name = name
            self.gpa = gpa
            self.credits = credits
    

    def display_info(self):
        return print(f"Student: name {self.name} - GPA {self.gpa} - credits: {self.credits}")
    
    def add_credits(self, amount):
        if (amount < 0):
            print("Amount of credits must be greater 0")
        else:
            self.__credits += amount
    
    def update_gpa(self, value):
        if ((0.0 > value) or (value > 4.0)):
            print("Student GPA must be between 0.0 and 4.0")
        else:
            self.gpa = value
