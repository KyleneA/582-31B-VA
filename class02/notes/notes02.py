# book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = Book("Lake", "Banana Yoshimoto", 10.99)
book2 = Book("Kitchen", "Banana Yoshimoto", 10.99)

print(book1.price)

book1.price = 100.99

print(book1.price)

class Product:
    def __init__(self, name, price, stock = 0):
        self.name = name
        self.price = price
        self.stock = stock

p1 = Product("Keyboard", 50, 10)
p2 = Product("Mouse", 20)


