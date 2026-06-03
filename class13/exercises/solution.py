# 1
# Create a parent class:

#   Animal
#   method: speak()

# then child classes:
#   Dog
#   Cat

# Override speak in ceach child!
# Dog says "Woof"
# Cat says "Meow"

# Then loop through them polymorphically

class Animal:
    def speak(self):
        print("Animal Sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()

# 2
# Create a parent class: Vehicle
# Child classes Car and Bike

# they share:
#   brand
#   describe()

# add child-specific behaviour

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def describe(self):
        print(f"The vehicle's brand is {self.brand}")

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def describe(self):
        print(f"The car's brand is {self.brand}")

class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def describe(self):
        print(f"The bike's brand is {self.brand}")

vehicles = [Vehicle("Ford"), Car("Kia"), Bike("Rocky Mountain")]

for vehicle in vehicles:
    vehicle.describe()


# 3
# parent class: Account
#               show_type()

# children accounts: SavingsAccount & PremiumAccount
#   override or extend behaviour accordingly

class Account:
    def __init__(self, owner):
        self.owner = owner

    def show_type(self):
        return f"{self.owner} has a regular account"
    
class SavingsAccount(Account):
    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate

    def show_type(self):
        return f"{self.owner} has a saving account with an interest rate of {self.interest_rate}"
    

class PremiumAccount(Account):
    def __init__(self, owner, reward_level):
        super().__init__(owner)
        self.reward_level = reward_level

    def show_type(self):
        return f"{self.owner} has a premium account with a reward level of {self.reward_level}"
    
accounts = [Account("Kamyar"), SavingsAccount("Moe", 7.5), PremiumAccount("Evgeniya", "Gold")]

for account in accounts:
    print(account.show_type())