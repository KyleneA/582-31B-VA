# 1. identify visibility intent
class User:
    def __init__(self, username, email, password_hash):
        self.username = username
        self.__email = email
        self.__password_hash = password_hash

# which attributes are public? which are intended for internal use?
# email and password are internal use , username is public


# 2. redesign the following class to improve encapsulation
class Course:
    def __init__(self, title, seats):
        self.title = title
        self.seats = seats


# 3. Create StudentAccount class:

# public username
# internal __credits
# methods: add_credits() - use_credits() - show_credits()


# 4. Create a MovieTicket class:

# public movie_title
# internal available_seats
# methods: book_seat() - cancel_seat() - show_status()
