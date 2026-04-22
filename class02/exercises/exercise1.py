# in here, I want you to createa new class for a friend.

# i want you to take in 4-5 arguments, and initialize it.
class Friend:
    # initialize
    def __init__(self, name, last_name, age, hobby):
        self.name = name
        self.last_name = last_name
        self.full_name = name + " " + last_name # for example, if the name Jane and ln is Doe full name would be Jane Doe
        self.age = age
        self.hobby = hobby
    # create a function that shows their full information
    def print_info(self):
        print(self.name, self.age, self.hobby)

    # create a function that greets them! (with print)
    def greet(self):
        # inside print use the name variable
        print("Hello!", self.name, "How are you?")
        # print("Hello! " + self.name + " How are you?")
        # print(f"Hello! {self.name}, how are you?")

# create 3 instances
friend1 = Friend("Astrid", "Sanchez", 24, "Dancing")
friend2 = Friend("Rama", "Chaker", 1, "Coding")
friend3 = Friend("John", "Doe", 18, "Football")

friend1.greet()
friend2.greet()
friend3.greet()

friend1.print_info()