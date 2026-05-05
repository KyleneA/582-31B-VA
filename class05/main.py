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

Student.show_school() # the method is not about one specific student!
                      # it is about the whole class!

print()
# compare them directly:
    # instance methods:
        # first parameter : self (ALWAYS!)
        # uses only one object
    
    # Class method:
        # first parameter : cls (ALWAYS!)
        # uses the class
class Product:
    count = 0

    def __init__(self, name):
        self.name = name
        self.increment_count()
        # Product.count += 1
    
    # class method that accesses class attribute
    @classmethod
    def show_count(cls):
        print(f"Total products: {cls.count}")

    # class method that updates a shared class attribute
    @classmethod
    def increment_count(cls):
        cls.count += 1

p1 = Product("Keyboard")
p2 = Product("Mouse")
p3 = Product("Keyboard")

Product.show_count()

