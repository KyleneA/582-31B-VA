class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    @classmethod
    def from_string(cls, data):
        name, price, category = data.split(",")
        return cls(name, int(price), category)
    
    @classmethod
    def from_dict(cls, data):
        name = data["name"]
        price = data["price"]
        category = data["category"]
        return cls(name, price, category)
    
    @classmethod
    def product_under_dev(cls, name):
        return cls(name,0,"")

prod1 = Product("something", 0, "something else")
print("prod1: ", prod1.name, prod1.price, prod1.category)

example_dict = {
    "name": "something",
    "price" : 1,
    "category": "something else"
}

prod2 = Product.from_dict(example_dict)
print("prod2: ", prod2.name, prod2.price, prod2.category)

ex_str = "something,2,something else"
prod3 = Product.from_string(ex_str)
print("prod3: ", prod3.name, prod3.price, prod3.category)

prod4 = Product.product_under_dev("something")
print("prod4: ", prod4.name, prod4.price, prod4.category)