## Interfaces & Abstraction
> [!def]
> Looks at what a whole category of objects should be able to do
> 
>> Abstraction
>> focusing on the essential behaviour, while hiding unnecessary details.
>
>> Interface
>> coding contract for classes (method blueprint)
 
Allows us to have:
1. clearer design
2. less duplication
3. easier extension
4. more consistent behaviour
5. (in larger code bases) better teamwork & maintainability

### Using interfaces in python
abstract base classes using the abs module
- import interfaces module
	- CANNOT be instantiated directly -> to be used in a concrete class
	```python
	from abc import ABC, abstractmethod
	
	class Shape(ABC): # ABC means that this class is abstract
		@abstractmethod
		def area(self):
			pass 
	```
- Instantiate in a concrete class
	- creates contract that all concrete shapes that are shape class type must have an area method
	```python
	class Rectangle(Shape):
		def __init__(self, width, height):
			self.width = width
			self.height = height
		
		def area(self):
			return self.width * self.height
	
	class Circle(Shape):
		def __init__(self, radius):
			self.radius = radius
		
		def area(self):
			return 3.14 * self.radius * self.radius
	
	rectangle = Rectangle(2, 4)
	circle = Circle(3)
	
	print(f"rectangle area is: {rectangle.area()}; circle area is: {circle.area()}")
	```
- we can then create functions that use abstract class methods
	```python
	def print_area(Shape):
		print(Shape.area())
	
	print_area(rectangle)
	print_area(circle)
	```

### When to use
- when several classes must follow the same contract
- when theres a shared behaviour
- when we want consistency