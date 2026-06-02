#Inheritance

# what happens when several classes are related and should share common behaviour
# without duplicating code??

# but first, let's do a quick recap:

# Encapsulation:

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    
# Encapsulation says: object state shold be protected intentionally.

# Properties:

# let us keep clean attribute syntax
# validate and/or controll access to our attributes

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

    @property
    def gpa(self):
        return self.__gpa ## define private attribute
    
    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0: # This is an invariant!
            self.__gpa = value
        else:
            raise ValueError("Invalid GPA")

# properties make controlled access feel natural!


# Invariants:

# what is an invariant? it's a rule that must always remain true
# good classes prevent invalid states


# Constans and Enums


from enum import Enum

# once value is set, you cannot change it in runtime in Pythonn
class CourseStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"

status = CourseStatus.OPEN

print(status.value)

# enums reduce invalid values and improve readability.

# for example: CourseStatus class becomes a container for a series of constants.


# all of the concepts above help us design one class properly. 