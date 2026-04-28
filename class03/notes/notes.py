# conditions indide of a method
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell_one(self):
        if self.stock > 0:
            self.stock = self.stock - 1
            print(f"Sold 1 {self.name}. now we have {self.stock} left")
        else:
            print(f"{self.name} is out of stock")

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

book1 = Book("Kitchen", "Banana Yoshimoto")
book1.borrow()
book1.borrow()
book1.show_status()

book2 = Book("Lake", "Banana Yoshimoto", False)
book2.borrow()
book2.return_book()
book2.show_status()

