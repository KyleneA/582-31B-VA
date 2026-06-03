# try:
#     number = int(input("Enter a number: "))
#     print("You entered: ", number)
#     print()
# except ValueError:
#     print("Invalid input")
#     print()

# try:
#     number = int(input("Enter a number: "))
#     print("You entered: ", number)
#     print()
# except ValueError as error:
#     print("Error: ", error)
#     print()

# # Multiple except blocks
# try:
#     x = int(input("Enter Numerator: "))
#     y = int(input("Enter Denominator: "))
#     division = x / y
#     print(division)
#     print()
# except ValueError:
#     print("please enter valid integer")
#     print()
# except ZeroDivisionError:
#     print("You cannont divide by zero")
#     print()

# # else
# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Conversion failed")
# else: # only runs if no error raised
#     print("Conversion Successful")

# finally block
try:
    x = int(input("Enter Numerator: "))
    y = int(input("Enter Denominator: "))
    division = x / y
except ZeroDivisionError as error:
    print("Error: ", error)
except ValueError as error:
    print("Error: ", error)
else:
    print(division)
    print("Division operation was successful")
finally:
    print("Operation is over")
    print()
