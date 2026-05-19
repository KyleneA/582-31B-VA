# Exercise 01
class Student:
    def __init__(self, name, gpa):
        if (0.0 <= gpa <= 4.0):
            self.name = name
            self.__gpa = gpa
        else:
            print("Please enter valid GPA")
    
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, new_gpa):
        if (0.0 <= new_gpa <= 4.0):
            self.__gpa = new_gpa
        else:
            print("Please enter valid GPA")

student = Student("Bob", 3.6)
print("Bob: ", student.gpa)
student.gpa = 4.0
print("Bob: ", student.gpa)
print()

# Exercise 02
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Price must be a positive number")

product = Product("Bench", 150)
print("Bench: ", product.price)
product.price = 100
print("Bench: ", product.price)
product.price = -100
print()

# Exercise 03
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return 3.1415 * (self.radius * self.radius)

circle = Circle(2)
print(circle.area)
print()

# Exercise 04
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.__last_name = last_name
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.__last_name}"

person = Person("Bob", "builder")
print(person.full_name)
print()

# Exercise 05
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value > 0:
            self.__balance = value
        else:
            print("Balance cannot be a negative value")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be a postitive value")
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        else:
            print("Deposit amount must be a postitive value")

acc = Account("Rob", 200)
print(acc.balance)
acc.deposit(-50)
print(acc.balance)
acc.deposit(50)
print(acc.balance)
acc.withdraw(-50)
print(acc.balance)
acc.withdraw(50)
print(acc.balance)
print()

