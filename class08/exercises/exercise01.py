# Exercise 1
## public attribute: username
## private attributes: email, password_hash

# Exercise 2
class Course:
    def __init__(self, title, seats):
        self.__title = title
        self.seats = seats

# Exercise 3
class StudentAccount:
    def __init__(self, username, credits):
        self.username = username
        self.__credits = credits
    
    def add_credits(self, amount):
        if (amount > 0):
            self.__credits += amount
    
    def use_credits(self, amount):
        if (0 < amount <= self.__credits):
            self.__credits -= amount
    
    def show_credits(self):
        print(f"Credit balance is {self.__credits}")

print()
acc = StudentAccount("Jo", 20)
acc.add_credits(5)
acc.show_credits()
acc.use_credits(10)
acc.show_credits()

# Exercise 4
class MovieTicket:
    def __init__(self, movie_title, available_seats):
        self.movie_title = movie_title
        self.__available_seats = available_seats
    
    def book_seat(self):
        if (self.__available_seats > 0):
            self.__available_seats -= 1
    
    def cancel_seat(self):
        self.__available_seats += 1
    
    def show_status(self):
        print(f"{self.movie_title} has {self.__available_seats} left")

print()
movie = MovieTicket("Totoro", 15)
movie.book_seat()
movie.show_status()
movie.cancel_seat()
movie.show_status()