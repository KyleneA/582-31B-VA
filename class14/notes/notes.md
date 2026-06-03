## Exceptions

### Basic `try/except`
```python
try:
    number = int(input("Enter a number: "))
    print("You entered: ", number)
    print()
except ValueError:
	print("Invalid input")
```

### Alternate way to write `try/except`
```python
try:
    number = int(input("Enter a number: "))
    print("You entered: ", number)
except ValueError as error:
	print("Error: ", error)
```

### Multiple blocks
```python
try:
    x = int(input("Enter Numerator: "))
    y = int(input("Enter Denominator: "))
    division = x / y # trying some code that could break
except ZeroDivisionError as error:
    print("Error: ", error) # raising error if denominator is 0
except ValueError as error:
    print("Error: ", error) # raising error if input isn't a number
else:
    print(division) # executes only when try is successful
    print("Division operation was successful")
finally:
    print("Operation is over") # always executes no matter what
    print()
```

## Class Design
### Common python Errors that is used in class design
- ValueError
- ZeroDivisionError
- KeyError
- TypeError
- IndexError
### Creating custom errors
```python
class InvalidGPAError(Exception): # creating the custom error
    pass

class StudentRecord:
    def __init__(self, name, gpa):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.__name = name
        self.gpa = gpa
    
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if not(0.0 <= value <= 4.0):
	        # using the custom error
            raise InvalidGPAError("GPA must be between 0.0 and 4.0")
        self.__gpa = value
```