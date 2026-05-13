class Student:
	def __init__(self, name, gpa):
		self.name = name # public attribute
		self.__gpa = gpa # private attribute

ex2 = Student("Sam", 4)
# print(ex2.__gpa) # -> causes error because of name mangling
print(ex2.__dict__)
print(ex2._Student__gpa)

# Properly Encapsulating
class BankAccount:
	def __init__(self, owner, balance):
		self.owner = owner
		self.__balance = balance # private
		# __balance is signaling internal use (within class itself)
	
	def deposit(self, amount):
		if (amount > 0):
			self.__balance += amount
	
	def withdraw(self, amount):
		if (0 < amount <= self.__balance):
			self.__balance -= amount
	
	def show_balance(self):
		print(f"Balance is: ${self.__balance}")

ex3 = BankAccount("Loo", 45)
ex3.deposit(15)
ex3.show_balance()
ex3.withdraw(5)
ex3.show_balance()