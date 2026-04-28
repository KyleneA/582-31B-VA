class User:
    def __init__(self, username, password):
        if len(password) < 4:
            print("User creation failed. Password needs to be at least 4 characters long")
        else:
            self.username = username
            self.password = password
    def set_password(self, new_password):
        if len(new_password) < 4:
            print("Password was not changed. Password needs to be at least 4 characters long")
        else:
            self.password = new_password

user1 = User("bob", "yo")
user2 = User("rob", "yogurt")
user3 = User("blob", "young")

user2.set_password("yop")