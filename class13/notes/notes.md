## Inheritance

### `super()`
> [!meaning]
> Go to the parent class 

- Can be used to initialize parent constructor + add on to it in child class
```python
class User:
    def __init__(self, username):
        self.username = username
        print(f"Step 1: ({self.username}) Parent constructor")

    def introduce(self):
        print(f"Hello, my name is {self.username}")

class StudentUser(User):
    def __init__(self, username, program):
        super().__init__(username) # super means to go to parent class -> here for constructor
        print(f"Step 2: ({self.username}) Child constructor")
        print()

        self.program = program
```
## Polymorphism
> [!meaning]
> different data types, objects, or functions can respond to the **same method** call in *their own way (differently)*

```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Employee(Person):
    def __init__(self, name, dpt):
        super().__init__(name)
        
        self.dpt = dpt
    
    # overriding the parent method
    def introduce(self):
        print(f"Hello, my name is {self.name} and I work at the {self.dpt}")

class Admin(Person):
    def __init__(self, name, dpt):
        super().__init__(name)
        self.dpt = dpt

    # override + use the parent method
    def introduce(self):
        super().introduce() # first execute parent method
        print(f"I oversee the {self.dpt} department") # then add the extra stuff

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, my name is {self.name} and I teach {self.subject}")

for person in people:
    person.introduce()
```
