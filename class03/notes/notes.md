## Methods
> [!definition]
> function defined inside of a class that represents behaviour belonging to an object

### Conditions in methods
#### Example 1
```python
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
```
#### Example 2
```python
# practicing method-writing
class Book:
    def __init__(self, title, author, available = True):
        self.title = title #string
        self.author = author #string
        self.available = available #boolean
        print(f"{self.title} was added successfully")

    def borrow(self):
        if (self.available == False):
            print(f"{self.title} is already borrowed")
        else:
            self.available = False
            print(f"{self.title} has been borrowed")
    
    def return_book(self):
        if (self.available == False):
            self.available = True
            print(f"{self.title} has been returned")
        else:
            print(f"I don't think that is my copy of {self.title}.")
    
    def show_status(self):
        print(f"{self.title} by {self.author} available: {self.available}")

book1 = Book("Kitchen", "Banana Yoshimoto") # -> Kitchen was added successfully
book1.borrow() # -> Kitchen has been borrowed
book1.borrow() # -> Kitchen is already borrowed
book1.show_status() # -> Kitchen by Banana Yoshimoto available: False

book2 = Book("Lake", "Banana Yoshimoto", False) # -> Lake was added successfully
book2.borrow() # -> Lake is already borrowed
book2.return_book() # -> Lake has been returned
book2.show_status() # -> Lake by Banana Yoshimoto available: True
```
## convention
> [!python]
> Generally, use of underscore for naming

## class review exercise
```python
class Fruit:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_category(self):
        return self.category
    
    def set_price(self, new_price):
        self.price = new_price
        return self.price

fruit1 = Fruit("banana", 2.99, "berry")
print(fruit1.get_name(), fruit1.get_category(), fruit1.get_price())
print(fruit1.set_price(0.99))
```

## Common Mistakes
```python
# mistake 1 -- forgetting self
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell_one(): # WE NEED TO PASS SELF AS A PARAMETER , ALWAYS!!!!!!
        self.stock -= 1


# mistake 2 -- forgeting self. for attributes!
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell_one(self):
        stock -= 1 # if you don't put self. before attribute name , it won't recognize it! IMPORTANT!!!

product = Product("test", 1)
print(product.stock)
product.sell_one()
print(product.stock)

# Mistake 3
Product.sell_one() # THIS IS NOT CORRECT, DONT CALL CLASS NAME (Product vs product--instance)
# product.sell_one()

# Mistake 4
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell_one(self):
        # this doesn't change anything! MISTAKE!
        self.stock - 1

        # these are statements, changing state CORRECTLY
        self.stock = self.stock - 1
        self.stock -= 1

# Mistake 5
# dont mix printing and returning with eachoter!
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def get_name(self):
        # these two are NOT EQUAL
        print(self.name) # used for quick demonstration
        return self.name # when the result/value needs to be stored/used elsewhere
```