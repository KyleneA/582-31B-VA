## Encapsulation
> [!definition]
> **Used to protect our code from ourselves**
> keeping data & the rules to use the data INSIDE the class
> - limiting direct access to internal details
> - protecting object state from invalid changes
> - exposing cleaner public interface
> => **classes used to help control how data is used**
### Naming Patterns for Visibility
Private vs Public data
- private: can't be directly accessed outside the class
- public: can be accessed directly inside & outside
> [!important]
> in python, we only use naming conventions and developer responsibility to show private vs public rather than compiler-enforced rules

#### Public
No symbols around variable names
```python
# examples
variable = "hi"

class Student:
	def __init__(self, name):
		self.name = name

ex1 = Student("Bob")
ex1.name = "Joe" # public attribute, can be changed outside class
```
#### Private
Has two underscores before variable names (`__variable`)
Name mangling: 
	- python preventing accidental overriding of data information
	- internally, python changes the variable name to `_ClassName__variable`
```python
__variable = "hi"

class Student:
	def __init__(self, name, gpa):
		self.name = name
		self.__gpa = gpa # private attribute

ex2 = Student("Sam", 4)
print(ex2.__gpa) # -> causes error (__gpa attribute doesn't exist) because of name mangling
print(ex2.__dict__) # __dict__ displays object as string -> {'name': 'Sam', '_Student__gpa': 4}
print(ex2._Student__gpa) # writing the attribute like this allows us to access it
```
#### Protected
Has 1 underscore before variable name(`_variable`)
```python

```