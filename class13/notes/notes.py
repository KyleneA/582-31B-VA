class User:
    def __init__(self, username):
        self.username = username
        print(f"Step 1: ({self.username}) Parent constructor")

    def introduce(self):
        print(f"Hello, my name is {self.username}")

class StudentUser(User):
    def __init__(self, username, program):
        super().__init__(username) # super means to go to parent class -> here for constructor
        print(f"Step 2: ({self.username}) Child constructor")
        print()

        self.program = program

class AdminUser(User):
    def __init__(self, username, dpt):
        super().__init__(username)
        print(f"Step 2: ({self.username}) Child constructor")
        print()
    
        self.dpt = dpt

student1 = StudentUser("bob_builds", "web dev")
student1.introduce() # function from parent class
print(f"Student program: {student1.program}")

try:
    print(f"Student department: {student1.dpt}")
except AttributeError as e:
    print("Error: ", e)
    print()

admin1 = AdminUser("john", "accounting")
admin1.introduce()
try:
    print(f"Admin program: {admin1.program}")
except AttributeError as e:
    print("Error: ", e)

print(f"Admin department: {admin1.dpt}")
print()