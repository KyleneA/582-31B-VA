from abc import ABC, abstractmethod

print("Exercise 1")

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("You drive the car to move")

class Bicycle(Vehicle):
    def move(self):
        print("You pedal to move the bicycle")

car1 = Car()
bike1 = Bicycle()

car1.move()
bike1.move()

print()
print("Exercise 2")

class FileHandler(ABC):
    @abstractmethod
    def read(self, file):
        pass

    @abstractmethod
    def write(self, file):
        pass

class TextFileHandler(FileHandler):
    def read(self, file):
        print(f"The {file} text file has been read")
    
    def write(self, file):
        print(f"Content has been written to {file} as a text file")

class JsonFileHandler(FileHandler):
    def read(self, file):
        print(f"The {file} JSON file has been read")
    
    def write(self, file):
        print(f"Content has been written to {file} as a JSON file")

txtFile = TextFileHandler()
JSONFile = JsonFileHandler()
txtFile.read("file_name")
txtFile.write("file_name")
JSONFile.read("file_name")
JSONFile.write("file_name")

print()
print("Exercise 3")

class Account(ABC):
    @abstractmethod
    def calculate_fee(self):
        pass

class SavingsAccount(Account):
    monthly_fee = 5.99

    def calculate_fee(self):
        return self.monthly_fee * 12

class PremiumAccount(Account):
    monthly_fee = 25.99

    def calculate_fee(self):
        return self.monthly_fee * 12

savingsAcc = SavingsAccount()
premiumAcc = PremiumAccount()
print(f"savingsAcc fee: {savingsAcc.calculate_fee()}, premiumAcc fee: {premiumAcc.calculate_fee()}")

print()
print("Exercise 4")

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    hourly_wage = 44.44
    weekly_hours = 40
    weeks_paid = 52

    def calculate_salary(self):
        return self.hourly_wage * self.weekly_hours * self.weeks_paid

class PartTimeEmployee(Employee):
    hourly_wage = 15
    weekly_hours = 20
    weeks_paid = 32

    def calculate_salary(self):
        return self.hourly_wage * self.weekly_hours * self.weeks_paid

ftEmployee = FullTimeEmployee()
ptEmployee = PartTimeEmployee()

print(f"full-time salary: {ftEmployee.calculate_salary()}")
print(f"part-time salary: {ptEmployee.calculate_salary()}")

print()
print("Exercise 5")

class Media(ABC):
    @abstractmethod
    def play(self, media):
        pass

class Song(Media):
    def play(self, media):
        print(f"The {media} song is playing")


class Video(Media):
    def play(self, media):
        print(f"Video {media} is now playing")

song = Song()
video = Video()

song.play("Bad by Michael Jackson")
video.play("Baby shark")