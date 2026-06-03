from enum import Enum

class AccountType(Enum):
    SAVINGS = "savings"
    CHEQUING = "chequing"
    INVESTMENT = "investement"



class Account:
    def __init__(self, owner, acc_type, balance):
        if (owner == ""):
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