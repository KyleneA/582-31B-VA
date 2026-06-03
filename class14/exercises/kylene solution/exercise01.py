from enum import Enum

class AccountType(Enum):
    SAVINGS = "savings"
    CHEQUING = "chequing"
    INVESTMENT = "investement"

class Account:
    def __init__(self, owner, acc_type, balance):
        if (owner.strip() == ""):
            raise ValueError("Owner cannot be empty")
        if not (isinstance(acc_type, AccountType)):
            raise ValueError("Account type must be a member of AccountType")
        
        self.__owner = owner
        self.__acc_type = acc_type
        self.balance = balance
    
    @staticmethod
    def isNumber(value):
        return type(value) == int or type(value) == float

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if not self.isNumber(value):
            raise ValueError("Account balance must be a number")
        self.__balance = value

    def deposit(self, amount):
        if not self.isNumber(amount):
            raise ValueError("Amount deposited must be a number")
        if amount < 0:
            raise ValueError("Amount deposited must a positive number")
        
        self.balance += amount
    
    def withdraw(self, amount):
        if not self.isNumber(amount):
            raise ValueError("Amount withdrawn must be a number")
        if amount < 0:
            raise ValueError("Amount withdrawn must a positive number")
        if amount > self.balance:
            raise ValueError(f"You have insufficient funds to withdraw ${amount}")
        self.balance -= amount

acc1 = Account("Bob", AccountType.CHEQUING, 100)

try:
    acc1.deposit(-1)
except ValueError as error:
    print("Error:", error)
finally:
    print(acc1.balance)

try:
    acc1.withdraw(-101)
except ValueError as error:
    print("Error:", error)
finally:
    print(acc1.balance)

try:
    acc1.deposit(1)
except ValueError as error:
    print("Error:", error)
finally:
    print(acc1.balance)

try:
    acc1.withdraw(101)
except ValueError as error:
    print("Error:", error)
finally:
    print(acc1.balance)

print()
print("============================")
print()

class Temperature:
    def __init__(self, celcius):
        if celcius < -273.15:
            raise ValueError("Celcius cannot be lower than absolute 0")
        self.celcius = celcius

try:
    temp1 = Temperature(-272)
except ValueError as error:
    print("Error: ", error)
else:
    print(temp1.celcius)

try:
    temp2 = Temperature(-274)
except ValueError as error:
    print("Error: ", error)
else:
    print(temp2.celcius)

print()
print("============================")
print()

class NegativePriceError(Exception):
    pass

class Product:
    def __init__(self, name, price):
        if name.strip() == "":
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise NegativePriceError("Product price cannot be a negative number")
        
        self.__name = name
        self.price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise NegativePriceError("Product price cannot be a negative number")
        self.__price = value
    
    def show_product(self):
        return f"Product: {self.__name}: ${self.price}"

try:
    prod1 = Product("mouse", -1)
except ValueError as error:
    print("Error: ", error)
except NegativePriceError as error:
    print("Error: ", error)
else:
    print(prod1.show_product())

print()

try:
    prod2 = Product(" ", 4)
except ValueError as error:
    print("Error: ", error)
except NegativePriceError as error:
    print("Error: ", error)
else:
    print(prod2.show_product())

print()

try:
    prod3 = Product("mouse", 15)
except ValueError as error:
    print("Error: ", error)
except NegativePriceError as error:
    print("Error: ", error)
else:
    print(prod3.show_product())