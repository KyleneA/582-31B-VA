# instance vs class methods
class Student:
    school_name = "ABC College"

    def __init__(self, name):
        self.name = name

    # instance method
    def introduce(self):
        print(f"my name is {self.name}")

    # class method
    @classmethod #as the mark to indicate not working with self -> otherwise will look for self
    def show_school(cls): # cls as signature / used instead of self
        print(f"School: {cls.school_name}") 
        # abstracted/ safer than using Student.school_name without affecting the whole class
        ## makes sure that you're refering to the class you are within

student1 = Student("John Doe")
student2 = Student("Jane Doe")

## instance method only works with one object at a time
student1.introduce()
student2.introduce()

## class method
Student.show_school() # gets information about 

print()

## Looking at HW exercise
class Product:
    count = 0

    def __init__(self, name):
        self.name = name
        self.increment_count() # to increase count when object instance created
    
    @classmethod
    def show_count(cls):
        print(f"Total product: {cls.count}")
    
    @classmethod
    def increment_count(cls):
        cls.count += 1

prod1 = Product("mouse")
prod2 = Product("camera")
Product.show_count()
print(f"prod1.count: {prod1.count}", f"prod2.count: {prod2.count}")

print()

# Design Pattern: Alternative Constructor
class Student:
    def __init__(self, name, program):
        self.name = name
        self.program = program
    
    @classmethod
    def from_string(cls, data):
        name, program = data.split(",")
        return cls(name, program)
    
    @classmethod
    def newly_admitted(cls, name):
        return cls(name, "")

stud1 = Student.from_string("Alice,web development")

# Static Methods
class Student:
    @staticmethod
    def is_valid_name(name):
        if (len(name.strip()) > 0):
            return True
        else:
            return False
    
    @staticmethod
    def format_grade(grade):
        return f"{grade:.2f}" # :.2f notation needs to be within f"" to work

# Instance methods:
    # no decorator (@ something)
    # first parameter: self (ALWAYS)
    # works with only one object
    # reads/modifies instance state

# Class methods:
    # decorator: @classmethod
    # first parameter is: cls (ALWAYS)
    # works with class-level state (class attributes, etc.)
    # often used for alternative constructors or shared behaviour

# Static methods:
    # decorator: @staticmethod
    # no self or cls 
    # usually used as utility/helper logic