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
    
    def new_price(self, new_price):
        self.price = new_price
        return self.price

fruit1 = Fruit("banana", 2.99, "berry")
print(fruit1.get_name(), fruit1.get_category(), fruit1.get_price())
print(fruit1.new_price(1.99))
