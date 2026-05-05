## Instance methods vs class methods
### Instance method
- first parameter is always `self`
- used only on ONE object
### Class methods
- Important to add `@classmethod` to indicate that the method will be working with `self`
- in place of `self` (for specific object instance of class), use `cls` to access class attributes
```python
# instance vs class methods
class Student:
    school_name = "ABC College"

    def __init__(self, name):
        self.name = name

    # instance method
    def introduce(self):
        print(f"my name is {self.name}")

    # class method
    @classmethod #as the mark to indicate not working with self -> otherwise will look for self
    def show_school(cls): # cls as signature / used instead of self
        print(f"School: {cls.school_name}") 
        # abstracted/ safer than using Student.school_name without affecting the whole class
        ## makes sure that you're refering to the class you are within

student1 = Student("John Doe")
student2 = Student("Jane Doe")

## instance method only works with one object at a time
student1.introduce()
student2.introduce()

## class method
Student.show_school() # gets information about 
```

## Design Pattern: Alternative Constructor
> [!definition]
> A class method that allows to create class objects using different input formats
> ex: comma separated strings (csv files), JSON, database row, dictionary

```python
class Student:
    def __init__(self, name, program):
        self.name = name
        self.program = program
    
    @classmethod
    def from_string(cls, data):
        name, program = data.split(",")
        return cls(name, program)

stud1 = Student.from_string("Alice,web development")
```

### Exercise
```python
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    @classmethod
    def from_string(cls, data):
        name, price, category = data.split(",")
        return cls(name, int(price), category) #price can be float(price) to allow decimals
    
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
```

## Dictionary
> [!definition]
> Maps a value to a key; like associative array from PHP
> Keys are usually strings
>> Formula:
>> ```
>> variable = {key1: value1, key2: value2, key3: value3, ...}
>> ``` 

## Static Methods
> [!Definition]
> belongs to class
> doesn't use `self` or `cls`
> marked with `@staticmethod`

- Static methods are usually used as helper functions
	- accessible to do something specific

## Instance vs Class vs Static Methods
- Instance methods:
    - no decorator (@ something)
    - first parameter: self (ALWAYS)
    - works with only one object
    - reads/modifies instance state

- Class methods:
    - decorator: @classmethod
    - first parameter is: cls (ALWAYS)
    - works with class-level state (class attributes, etc.)
    - often used for alternative constructors or shared behaviour

- Static methods:
    - decorator: @staticmethod
    - no self or cls 
    - usually used as utility/helper logic

## Common Mistakes
- forgetting `cls` in a class method
- using `self` in a class method
	- class methods DO NOT receive an instance
- using static method in place of class method
	- ex: method that needs access to class attributes
- using class method instead of  static method