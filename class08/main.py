# encapsulation

class Book:
    def __init__(self, name):
        self.name = name

book1 = Book("test")

book1.name = "something else"

print(book1.name)

# public -- data can be accessed from anywhere (inside or outside)
# private -- protects the data from being accessed DIRECTLY outside of the class.
#   ex: private name


# in Python, we only use naming conventions and developer responsibility

# Python trusts the programmer more
# visibility (public, private) is about communication and design, not just compiler-enforced rules!


# so far we've seen:

# classes
# instance attr.
# instance methods
# class attr.
# class methods
# static methods
# abstraction and interfaces

# let's bring in encapsulation here:

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

acc1 = BankAccount("Alice", 500)
acc1.balance = -1000

# we need to protect our code from ourselves!

# encapsulation means keeping data and the rules for using that data together inside the class.
# it also means:
#               limiting direct access to internal details
#               protecting object state from invalid changes
#               exposing a cleaner public interface


# we want our class to help control how that data is used.


# ============

# we have three naming patterns to signal intended visibility

# 1. public
name = "hi"

class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("John")
student1.name = "Ali"
# ^ this is a public attribute

# 2. private
__name = "hi"

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa # private attr.

student2 = Student("Alice", 3.8)
# print(student2.__gpa) # this would fail, because of the concept of name mangling



# 3. protected
_name = "hi"


# what is name mangling?

# when an attribute starts with __ inside a class, Python changes its internal name to reduce accidental
# access and accidental overriding.

student3 = Student("Jane", 3.5)
print(student3.__dict__) 
# ^ we see that __gpa has been transformed to _Student__gpa internally.

print(student3._Student__gpa)
# print(student3.__gpa) # this doesn't show anything and throws an error

# the goal of using this private accessor is to 
#   avoid accidental direct access
