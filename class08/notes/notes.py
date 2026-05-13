class Student:
	def __init__(self, name, gpa):
		self.name = name # public attribute
		self.__gpa = gpa # private attribute

ex2 = Student("Sam", 4)
# print(ex2.__gpa) # -> causes error because of name mangling
print(ex2.__dict__)
print(ex2._Student__gpa)

