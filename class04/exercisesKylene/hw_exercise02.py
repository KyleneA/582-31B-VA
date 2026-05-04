# Exercise 1
class Book:
    total_books = 0

    def __init__(self, id, name, author, year):
        self.id = id
        self.name = name
        self.author = author
        self.year = year

        Book.total_books += 1

b1 = Book("0001", "Kitchen", "Banana Yoshimoto", "1988")
b2 = Book("0001", "Lake", "Banana Yoshimoto", "2005")

# Exercise 2
class Student:
    school_name = "Vanier College"
    student_count = 0

    def __init__(self, name, program, grade):
        self.name = name
        self.program = program
        self.grade = grade

        Student.student_count += 1

    def display_info(self):
        print(f"{self.name} studies {self.program} at {self.school_name}. Grade: {self.grade}")

print(f"--- students ---")
stu1 = Student("bob", "maths", 88).display_info()
stu2 = Student("rob", "maths", 68).display_info()
stu3 = Student("ron", "maths", 78).display_info()

# Exercise 3
class Product:
    category = "Electronics"
    tax_rate = 0.15

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def price_with_tax(self):
        total_price = self.price * (1 + self.tax_rate)
        return total_price

prod1 = Product("calculator", 20)
prod2 = Product("mouse", 10)
prod3 = Product("keyboard", 100)

print(f"--- original ---")
print(prod1.price_with_tax(), prod2.price_with_tax(), prod3.price_with_tax())

Product.tax_rate = 0.2
print(f"--- 0.2 tax_rate ---")
print(prod1.price_with_tax(), prod2.price_with_tax(), prod3.price_with_tax())

# Exercise 4
class Employee:
    company_name = "TechNova"
    bonus_rate = 0.10
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.employee_count += 1
    
    def calculate_bonus(self):
        return self.salary * self.bonus_rate

    def display_employee(self):
        bonus = self.calculate_bonus()
        print(f"{self.name} works at {self.company_name}. Salary: {self.salary}. Bonus: {bonus}")

em1 = Employee("Bob", 40000)
em2 = Employee("Rob", 40000)
em3 = Employee("Ron", 40000)

print(f"--- original ---")
em1.display_employee()
em2.display_employee()
em3.display_employee()

em3.bonus_rate = 0.5

print(f"--- em3 bonus ---")
em1.display_employee()
em2.display_employee()
em3.display_employee()

Employee.bonus_rate = 0.05

print(f"--- Employee bonus ---")
em1.display_employee()
em2.display_employee()
em3.display_employee()

# em3 has a shadowed bonus_rate because I changed it to 0.5 at the em3 bonus section