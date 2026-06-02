# Exercise 1

class Animal:
    def speak(self):
        print("This animal is speaking to you")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("I am a dog and I say WOOF!")

class Cat(Animal):
    def speak(self):
        print("I am a cat and I MEOW at you!")

animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.speak()
    print()

# 2
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def describe(self):
        print(f"This vehicle is from the {self.brand} brand")
# Create a parent class: Vehicle
# Child classes Car and Bike

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
    
    def sound(self):
        print(f"This {self.brand} car makes a vroooooom sound as it passes you")

class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def signal(self):
        print(f"Ring ring, this {self.brand} bike is passing you")

vehicles = [
    Vehicle("Toyota"),
    Car("Nissan"),
    Bike("Norco")
]

for vehicle in vehicles:
    vehicle.describe()

    try:
        vehicle.sound()
    except AttributeError as e:
        print("Error: ", e)

    try:
        vehicle.signal()
    except AttributeError as e:
        print("Error: ", e)

    print()

