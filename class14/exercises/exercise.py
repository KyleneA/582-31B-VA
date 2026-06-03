# 1
# Create a class with:
#   private balance
#   deposit(amount)
#   withdraw(amount)
# 
# Use exceptions for:
#   negative deposit
#   negative withdrawal
#   insufficient funds

class DepositError(Exception):
    pass

class NegativeWithdrawalError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, value):
        if not value.strip():
            raise ValueError("Owner's name cannot be empty")
        self.__owner = value

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance should be more or equal to zero")
        self.__balance = value

    def deposit(self, amount):
        if amount < 0:
            raise DepositError("The amount to deposit should be a positive number")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeWithdrawalError("The amount withdrawn should be a positive number")
        if amount > self.balance:
            raise InsufficientFundsError("There is not enough money in your account")
        self.balance -= amount


# 2
# Create a class with:
#   property celsius
# 
# 
# Raise an exception if:
#   temperature is below absolute zero

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15: 
            raise ValueError("temperature cannot be below absolute zero")
        self.__celsius = value

try:
    temp = Temperature(-300)
except ValueError as e:
    print("Error: ", e)


# 3
# Create:
# class NegativePriceError(Exception):
#     pass

# Then use it in a Product class.

class NegativePriceError(Exception):
    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise NegativePriceError("Product price cannot be negative")
        
        self.__price = value

try:
    # p1 = Product("Laptop", 1000)
    # print(p1.name, p1.price)
    p = Product("Phone", -1000)
except NegativePriceError as error:
    print("Error: ", error)
else:
    print(p.name, p.price)
finally:
    print("Operation finished.")


