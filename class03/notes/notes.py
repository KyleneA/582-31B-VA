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

