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
        self.__seats = seats
    
    def add_seats(self, amount):
        self.__seats += amount
        print(f"{amount} seats added")

    def remove_seats(self, amount):
        if amount <= self.__seats:
            self.__seats -= amount
            print(f"{amount } seats removed")
        else:
            print("Not enough seats available")

    def show_seats(self):
        print(f"Available Seats: {self.__seats}")

# 3. Create StudentAccount class:

# public username
# internal __credits
# methods: add_credits() - use_credits() - show_credits()

class StudentAccount:
    def __init__(self, username, credits):
        self.username = username
        self.__credits = credits

    def add_credits(self, amount):
        if amount > 0:
            self.__credits += amount
        else:
            print("Amount is invalid!")
        
    def use_credits(self, amount):
        # if 0 < amount and amount <= self.__credits:
        if 0 < amount <= self.__credits:
            self.__credits -= amount
        else:
            print("Amount is invalid!")
    
    def show_credits(self):
        print(f"You have {self.__credits} credits!")
        # return self.__credits


# 4. Create a MovieTicket class:

# public movie_title
# internal available_seats
# methods: book_seat() - cancel_seat() - show_status()

class MovieTicket:
    def __init__(self, movie_title, available_seats):
        self.movie_title = movie_title
        self.__available_seats = available_seats

    def book_seat(self, seats):
        if self.__available_seats > seats > 0:
            self.__available_seats -= seats
        else:
            print("There are no more available seats, womp womp")

    def cancel_seat(self, seats):
        if seats > 0:
            self.__available_seats += seats
        else:
            print("Wrong amount")

    def show_status(self):
        print(f"For {self.movie_title}: There are {self.__available_seats} seats available!") 