from users import User, Customer, Staff
from movie import MovieShow
from theater import ShowStatus
from customExceptions import InvalidBookingError, ShowSoldOutError, ShowCancelledError, InvalidStatusError

print("==========Customer==========")
try:
    customer1 = Customer("Bob", "bob.email.com")
    print(customer1.display_info())
except ValueError as error:
    print("ERROR:", error)
try:
    customer1 = Customer("", "bob@email.com")
    print(customer1.display_info())
except ValueError as error:
    print("ERROR:", error)
try:
    customer1 = Customer("  ", "bob@email.com")
    print(customer1.display_info())
except ValueError as error:
    print("ERROR:", error)
try:
    customer1 = Customer("Bob", "bob@email.com")
    customer2 = Customer("Rob", "rob@email.com")
    print(customer1.display_info(), customer2.display_info())
except ValueError as error:
    print("ERROR:", error)

print("==========Staff==========")
try:
    staff1 = Staff("Bob", "bob.email.com")
    print(staff1.display_info())
except ValueError as error:
    print("ERROR:", error)
try:
    staff1 = Staff("", "bob@email.com")
    print(staff1.display_info())
except ValueError as error:
    print("ERROR:", error)
try:
    staff1 = Staff("  ", "bob@email.com")
    print(staff1.display_info())
except ValueError as error:
    print("ERROR:", error)
try:
    staff1 = Staff("Bob", "bob@email.com")
    staff2 = Staff("Rob", "rob@email.com")
    print(staff1.display_info(), staff2.display_info())
except ValueError as error:
    print("ERROR:", error)

print("==========MovieShow==========")
try:
    movie1 = MovieShow("", 30)
    print(movie1.display_info())
except ValueError as error:
    print("ERROR:", error)
except InvalidBookingError as error:
    print("BOOKING ERROR:", error)
except ShowSoldOutError as error:
    print("SOLD OUT ERROR:", error)
except ShowCancelledError as error:
    print("SHOW CANCELLED ERROR:", error)
except InvalidStatusError as error:
    print("STATUS ERROR:", error)
try:
    movie1 = MovieShow("Totoro", -30)
    print(movie1.display_info())
except ValueError as error:
    print("ERROR:", error)
except InvalidBookingError as error:
    print("BOOKING ERROR:", error)
except ShowSoldOutError as error:
    print("SOLD OUT ERROR:", error)
except ShowCancelledError as error:
    print("SHOW CANCELLED ERROR:", error)
except InvalidStatusError as error:
    print("STATUS ERROR:", error)
try:
    movie1 = MovieShow("Totoro", 30, -2)
    print(movie1.display_info())
except ValueError as error:
    print("ERROR:", error)
except InvalidBookingError as error:
    print("BOOKING ERROR:", error)
except ShowSoldOutError as error:
    print("SOLD OUT ERROR:", error)
except ShowCancelledError as error:
    print("SHOW CANCELLED ERROR:", error)
except InvalidStatusError as error:
    print("STATUS ERROR:", error)
try:
    movie1 = MovieShow("Totoro", 30, 32)
    print(movie1.display_info())
except ValueError as error:
    print("ERROR:", error)
except InvalidBookingError as error:
    print("BOOKING ERROR:", error)
except ShowSoldOutError as error:
    print("SOLD OUT ERROR:", error)
except ShowCancelledError as error:
    print("SHOW CANCELLED ERROR:", error)
except InvalidStatusError as error:
    print("STATUS ERROR:", error)
try:
    movie1 = MovieShow("Totoro", 30, 2, "open")
    print(movie1.display_info())
except ValueError as error:
    print("ERROR:", error)
except InvalidBookingError as error:
    print("BOOKING ERROR:", error)
except ShowSoldOutError as error:
    print("SOLD OUT ERROR:", error)
except ShowCancelledError as error:
    print("SHOW CANCELLED ERROR:", error)
except InvalidStatusError as error:
    print("STATUS ERROR:", error)
try:
    movie1 = MovieShow("Totoro", 20)
    print(movie1.display_info())
    movie1.book_tickets(customer1, 10)
    print(movie1.display_info())
    movie1.book_tickets(customer2, 10)
    print(movie1.display_info())
    movie1.book_tickets(customer1, 15)
    print(movie1.display_info())
except ValueError as error:
    print("ERROR:", error)
except InvalidBookingError as error:
    print("BOOKING ERROR:", error)
except ShowSoldOutError as error:
    print("SOLD OUT ERROR:", error)
except ShowCancelledError as error:
    print("SHOW CANCELLED ERROR:", error)
except InvalidStatusError as error:
    print("STATUS ERROR:", error)
try:
    movie2 = MovieShow("Ponyo", 30, 2, ShowStatus.OPEN)
    print(movie2.display_info())
    movie2.cancel_show()
    print(movie2.display_info())
    movie2.book_tickets(Customer("Bob", "bob@email.com"), 2)
    print(movie2.display_info())
except ValueError as error:
    print("ERROR:", error)
except InvalidBookingError as error:
    print("BOOKING ERROR:", error)
except ShowSoldOutError as error:
    print("SOLD OUT ERROR:", error)
except ShowCancelledError as error:
    print("SHOW CANCELLED ERROR:", error)
except InvalidStatusError as error:
    print("STATUS ERROR:", error)