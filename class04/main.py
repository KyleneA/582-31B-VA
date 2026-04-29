# Class attributes vs instance attributes

class Student:
    def __init__(self, name, program):
        self.name = name
        self.program = program

student1 = Student("Alice", "Web Development")
student2 = Student("Karim", "Computer Science")

print(student1.name)
print(student2.name)

# what if all students were from the same school?

# the idea is:
    # some data belongs to:
    #   each object individually
    # Other data belongs to:
    #   the whole class

# instance attribute --> per-object state
# class attribute --> shared class-level state

class Student:
    school_name = "Vanier College" # This is our shared class attribute

    def __init__(self, name, program):
        # these are instance attributes / per-object state
        self.name = name
        self.program = program

student1 = Student("Alice", "Web Development")
student2 = Student("Karim", "Computer Science")

print(student1.name)
print(student2.name)

print(student1.school_name)
print(student2.school_name)

Student.school_name = "ABC College" # we can change the shared attribute directly for all instances of a class.
print('----')
print(student1.school_name)
print(student2.school_name)



# visual comparison:

    # Instance attributes:
    #   created with self
    #   usually set in __init
    #   different per object

    # Class attributes:
    #   defined in class body
    #   shared across all instances
    #   used for common data or class-level configuration
print('----')
class Product:
    category = "Electronics" # shared

    def __init__(self, name, price):
        self.name = name # per object
        self.price = price # per object

product1 = Product("Keyboard", 10)
product2 = Product("Mouse", 25)

product1.price = 8

print(product1.price)
print(product2.price)
print(product1.category)
print(product2.category)