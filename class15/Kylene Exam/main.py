from users import User, Customer, Staff, VIPCustomer
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
    print("Before trying to change", customer1.display_info(), customer2.display_info())
    customer1.name = "Joe"
    customer2.email = "new_rob@email.com"
    print("After trying to change", customer1.display_info(), customer2.display_info())
except ValueError as error:
    print("ERROR:", error)
try:
    customer3 = VIPCustomer("Bob3", "bob@email.com")
    customer4 = VIPCustomer("Rob4", "rob@email.com")
    print(customer3.display_info(), customer4.display_info())
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
    print("Before trying to change", staff1.display_info(), staff2.display_info())
    staff1.name = "Joe"
    staff2.email = "new_rob@email.com"
    print("After trying to change", staff1.display_info(), staff2.display_info())
except ValueError as error:
    print("ERROR:", error)

print("==========Polymorphism==========")
users = [User("Lam", "lam@email.com"), Customer("Sam", "sam@email.com"), Staff("Cam", "cam@email.com")]
for user in users:
    print(user.display_info())

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
    movie1.reopen_show()
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
try:
    movie3 = MovieShow("Mononoke Hime", 10, 9, ShowStatus.OPEN)
    print(movie3.display_info())
    movie3.book_tickets(Customer("Bob", "bob@email.com"), 3)
    print(movie3.display_info())
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
    movie4 = MovieShow("Spirited Away", 10, 10, ShowStatus.SOLD_OUT)
    print(movie4.display_info())
    movie4.book_tickets(Customer("Bob", "bob@email.com"), 4)
    print(movie4.display_info())
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
    movie4 = MovieShow("Spirited Away", 10, 10)
    print(movie4.display_info())
    movie4.book_tickets(Customer("Bob", "bob@email.com"), 4)
    print(movie4.display_info())
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