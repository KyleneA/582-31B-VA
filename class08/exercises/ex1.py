# 1. identify visibility intent

class User:
    def __init__(self, username, email, password_hash):
        self.username = username
        self.__email = email
        self.__password_hash = password_hash

# which attributes are public? which are intended for internal use?


# 2. redesign the following class to improve encapsulation
class Course:
    def __init__(self, title, seats):
        self.title = title
        self.seats = seats


