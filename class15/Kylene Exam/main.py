from users import User, Customer, Staff

print("==========Customer==========")
try:
    customer1 = Customer("Bob", "bob.email.com")
    print(customer1.display_info())
except ValueError as error:
    print(error)
try:
    customer1 = Customer("", "bob@email.com")
    print(customer1.display_info())
except ValueError as error:
    print(error)
try:
    customer1 = Customer("  ", "bob@email.com")
    print(customer1.display_info())
except ValueError as error:
    print(error)
try:
    customer1 = Customer("Bob", "bob@email.com")
    customer2 = Customer("Rob", "rob@email.com")
    print(customer1.display_info(), customer2.display_info())
except ValueError as error:
    print(error)

print("==========Staff==========")
try:
    staff1 = Staff("Bob", "bob.email.com")
    print(staff1.display_info())
except ValueError as error:
    print(error)
try:
    staff1 = Staff("", "bob@email.com")
    print(staff1.display_info())
except ValueError as error:
    print(error)
try:
    staff1 = Staff("  ", "bob@email.com")
    print(staff1.display_info())
except ValueError as error:
    print(error)
try:
    staff1 = Staff("Bob", "bob@email.com")
    staff2 = Staff("Rob", "rob@email.com")
    print(staff1.display_info(), staff2.display_info())
except ValueError as error:
    print(error)