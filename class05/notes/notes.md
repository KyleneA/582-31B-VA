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
