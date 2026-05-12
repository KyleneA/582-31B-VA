from abc import ABC, abstractmethod
	
class Shape(ABC): # ABC means that this class is abstract
    @abstractmethod
    def area(self):
        pass 

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

print()

def print_area(Shape):
    print(Shape.area())

print_area(rectangle)
print_area(circle)