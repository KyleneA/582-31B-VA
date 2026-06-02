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