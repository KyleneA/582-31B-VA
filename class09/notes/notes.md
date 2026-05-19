## Properties
> Allow simple attribute-style access while secretly adding validation and control behind the scenes
> - Managed by methods inside the class (with `@property` decoration)

> [!important]
> When creating the property in the class, cannot name the internal storage name (variable) and the property name the same because it will cause a recursive error (program not sure which one you are referring to and keeps calling itself)
```python
class Temperature:
    def __init__(self, celcius):
        self.__celcius = celcius # encapsulate to prevent easily changing

    @property # allows to write attribute like a method but access like an attribute
    def celcius(self): 
	    # gives more control over how the value changes (we can set it in the method)
        if value >= -273.15:
            self.__celcius = value
        else:
            print("Invalid temperature")
    
    # setter
    @celcius.setter
    def celcius(self, value):
        if value >= -273.15:
            self.__celcius = value
        else:
            print("Invalid temperature")

new_t = Temperature(25)
print(new_t.celcius) # prints 25
print("setting new values")
new_t.celcius = 30
print("setting to 30: ", new_t.celcius) # prints 30
new_t.celcius = -300 # prints "Invalid temperature"
print("after setting to -300: ", new_t.celcius) # prints 30
```

- Without a setter, the property is read-only protecting it from being changed
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property 
    def area(self): 
        return self.width * self.height

rectangle = Rectangle(20, 5)
print(rectangle.area)

rectangle.area = 50 # doesn't work because the property has no setter
```

### 2 Types of properties
- Stored managed properties
	- backed by internal state (the class)
	- often has getter and setter
	- ex: Temperature celcius attribute
- Computed read-only properties
	- derived from other attributes
	- may only need `@property`, no setter
	- ex: Rectangle area property