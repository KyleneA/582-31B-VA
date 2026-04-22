class Friend():
    def __init__(self, name, last_name, age, months_acquainted, common_interests):
        self.name = name
        self.last_name = last_name
        self.full_name = name + " " + last_name
        self.age = age
        self.months_acquainted = months_acquainted
        self.common_interests = common_interests

    def print_friend(self):
        print(self.full_name, self.age, self.months_acquainted, self.common_interests)

    def greet(self):
        print("Hello", self.name, "!")
        print(f"Greetings, {self.name}!")

friend1 = Friend("Bob", "Builder", 25, 12, "fixing things")
friend1.print_friend()
friend1.greet()

friend2 = Friend("Dora", "Explorer", 25, 22, "exploring new places")
friend2.print_friend()
friend2.greet()

friend3 = Friend("Thomas", "Train", 25, 32, "train watching")
friend3.print_friend()
friend3.greet()