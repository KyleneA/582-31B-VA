# Interfaces / Abstraction

# so far we've built concrete classes 

class Book:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Book name is: {self.name}")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product name is {self.name}")


# let's move one level higher than just concrete classes.

# instead of asking what one object does, we ask what a whole category of objects should be able to do.


# in the examples above, we see that our classes might behave in a similar way and we want to think of 
# abstraction as a way that allows us to design our code.

# in here, abstraction means focusing on the essential behaviour, while hiding unnecessary details.


# Imagine a payment system --> every payment method must have a pay(amount) operation

# but!!    a credit card pays one way -- PayPal pays another way -- bank transfer works differently , etc.

# the shared  idea for the above:  is the abstraction "a payment method can make a payment"

# abstraction allows us to have 
# 1. clearer design
# 2. less duplication
# 3. easier extension
# 4. more consistent behaviour
# 5. in case of larger code bases: better teamwork and maintainability

# let's get practical now!

