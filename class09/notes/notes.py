# without properties
class Temperature:
    def __init__(self, celcius):
        self.__celcius = celcius # encapsulate to prevent easily changing

    # using getter function can easily access attribute
    def get_celcius(self):
        return self.__celcius
    
    # with setter can more easily change the attribute value
    def set_celcius(self, value):
        if value >= -273.15:
            self.__celcius = value
        else:
            print("Invalid temperature")

t = Temperature(25)
print(t.get_celcius()) # prints 25
print()

# with properties
class Temperature:
    def __init__(self, celcius):
        self.__celcius = celcius # encapsulate to prevent easily changing

    @property # allows to write attribute like a method but access like an attribute
    def celcius(self):
        return self.__celcius
    
    # with a setter
    @celcius.setter
    def celcius(self, value):
        if value >= -273.15:
            self.__celcius = value
        else:
            print("Invalid temperature")

new_t = Temperature(25)
print(new_t.celcius) # prints 25
print("setting new values")
new_t.celcius = 30
print("setting to 30: ", new_t.celcius) # prints 30
new_t.celcius = -300 # prints "Invalid temperature"
print("after setting to -300: ", new_t.celcius) # prints 30
print()

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")

acc = BankAccount("Bob", 500)
print(acc.balance)

acc.balance = 300 # gives more control over how the value changes (we can set it in the method)
print(acc.balance)
print()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property 
    def area(self): # without a setter, property is read-only
        return self.width * self.height

rectangle = Rectangle(20, 5)
print(rectangle.area)

rectangle.area = 50 # doesn't work because the property has no setter