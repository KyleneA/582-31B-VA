# try:
#     number = int(input("Enter a number: "))
#     print("You entered: ", number)
#     print()
# except ValueError:
#     print("Invalid input")
#     print()

# try:
#     number = int(input("Enter a number: "))
#     print("You entered: ", number)
#     print()
# except ValueError as error:
#     print("Error: ", error)
#     print()

# # Multiple except blocks
# try:
#     x = int(input("Enter Numerator: "))
#     y = int(input("Enter Denominator: "))
#     division = x / y
#     print(division)
#     print()
# except ValueError:
#     print("please enter valid integer")
#     print()
# except ZeroDivisionError:
#     print("You cannont divide by zero")
#     print()

# # else
# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Conversion failed")
# else: # only runs if no error raised
#     print("Conversion Successful")

# # finally block
# try:
#     x = int(input("Enter Numerator: "))
#     y = int(input("Enter Denominator: "))
#     division = x / y
# except ZeroDivisionError as error:
#     print("Error: ", error)
# except ValueError as error:
#     print("Error: ", error)
# else:
#     print(division)
#     print("Division operation was successful")
# finally:
#     print("Operation is over")
#     print()

#==========================================

# Class design

# def set_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative!")
#     return age

# try:
#     set_age(int(input("Enter your age: ")))
#     print()
# except ValueError as error:
#     print("Error: ", error)


# Creating custom exception
class InvalidGPAError(Exception):
    pass

class StudentRecord:
    def __init__(self, name, gpa):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.__name = name
        self.gpa = gpa
    
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if not(0.0 <= value <= 4.0):
            raise InvalidGPAError("GPA must be between 0.0 and 4.0")
        self.__gpa = value

sr1 = StudentRecord("test", 4)

try:
    sr2 = StudentRecord("", 5)
except InvalidGPAError as error:
    print("Could not create student record, ", error)
except ValueError as error:
    print("Error: ", error)