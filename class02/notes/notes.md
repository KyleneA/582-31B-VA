## Classes
- meaningful entities: structured objects and reusable 

### Creating Classes
```python
class Student:
	pass # allows to create class without initializing 
```
### Initializing with required properties?
```python
class Student:
	# init function always called first when Student object is created.
	def __init__(self, name, program, gpa): # self refers to the object itself
		self.name = name
		self.program = program
		self.gpa = gpa
	
	#creating class function
	def print_info(self):
		print(self.name, self.program, self.gpa)
		# alternative with f string (like backtick)
		## print(f"Greetings, {self.name}!")

# creating a Student object
student1 = Student("Jane", "Web Development", 3.7)

# calling Class function
student1.print_info()
```

#### Default values
```python
class Product:
    def __init__(self, name, price, stock = 0):
        self.name = name
        self.price = price
        self.stock = stock
      
p1 = Product("Keyboard", 50, 10)
# p1.stock => 10
p2 = Product("Mouse", 20) # takes the default value from init function
# p2.stock => 0
```

### Common mistakes
```python
class Student1:
	# missing self in argument
	def __init__(name, program, gpa): # 
		self.name = name
		self.program = program
		self.gpa = gpa

class Student2:
	# arguments with default values need to be at the end of the list so that the order can be maintained
	def __init__(self, name, program = "", gpa): 
		self.name = name
		self.program = program
		self.gpa = gpa

class Student3:
	def __init__(self, name, age, program = "", gpa = 3): 
		self.name = name
		self.program = program
		self.gpa = gpa

s1 = Student3("bob", 12, gpa = 4) # positional argument
s2 = Student3("rob", 21, program = "psych", gpa = 3.3) # once a positional argument is called the following arguments must also be positional arguments

class Student4:
	def __init__(self, name, program, gpa): 
	# forgetting the "self."
		name = name
		program = program
		gpa = gpa

class Student5:
	def __init__(self, name, program, gpa): 
		self.name = name
		self.program = program
		self.gpa = gpa

s2 = Student5("bob", "maths", 3.5)
print(S2) # python is case sensitive so S2 doesn't exist

class Student6:
	# INDENTATIONS
	def __init__(self, name, program, gpa): 
	self.name = name #should be indented
	self.program = program #should be indented
	self.gpa = gpa #should be indented
	
	def print_info(self)
		print(self.name, self.program, self.gpa)
		
		def greet(self) # should remove 1 indentation
			print(f"Hello {self.name}!") # should remove 1 indentation
			
	s3 = Student6("bob", "maths", 4) # is still within the class/ should remove 1 indentation
```

### Terminology
```python
class Product: # this is our class
    def __init__(self, name): # this is a constructor
        self.name = name # this is a property

    def greet(self): # this is a method!
        print("hello")

# this is an instance of our object
p1 = Product("Banana")
```