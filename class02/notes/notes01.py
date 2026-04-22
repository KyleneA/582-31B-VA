class Student:
	# init function always called first when Student object is created.
	def __init__(self, name, program, gpa): # self refers to the object itself
		self.name = name
		self.program = program
		self.gpa = gpa
    
    #creating class function
	def print_info(self):
		print(self.name, self.program, self.gpa)

# creating a Student object
student1 = Student("Jane", "Web Development", 3.7)

print(student1.name, student1.program, student1.gpa)
student1.print_info()

