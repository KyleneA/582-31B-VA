# 2026-04-22 Notes

Today we talk about Object Oriented Programming!

First we start with classes.

Previously, in PHP we saw procedural, and even often page-based programming!

We try to keep the same logic for our database. However!

Meaningful entities.. so our users, products, orders, etc. as structured objects.

So a "class" in object oriented programming gives us that!

We need a reusable way to treat these structured objects.

Classes give us a way to define what we need to initialize an object.

Let's say, for a student all we need is the student's name, program, and gpa..
Let's say, for an employee, all we need is their name, address, id_number.

These are all here to help us write maintainable and REUSABLE code.

Some information for syntax:

`def **init**(...)`

- This is a special method automatically called when a new object is created.

`self`

- This refers to the specific object being initialized.

`self.name = name`

- This means:
  take the argument name
  store it inside the current object under the attribute/property name

### Some terminology:

```
class Product: # this is our class
    def __init__(self, name): # this is a constructor
        self.name = name # this is a property

    def greet(self): # this is a method!
        print("hello")

# this is an instance of our object
p1 = Product("Banana")
```
