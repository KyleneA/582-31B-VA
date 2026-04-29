class Employee:
    base_salary = 500
    bonus = 0.25
    company_name = "582-31B"

    def __init__(self, name, sales_count):
        self.name = name
        self.sales_count = sales_count
        print(f"Employee {self.name} has been created")
    
    def get_salary(self):
        if (self.sales_count > 10):
            bonus_salary = self.base_salary * (1 + self.bonus)
            return bonus_salary
        return self.base_salary

employee1 = Employee("Bob", 7)
employee2 = Employee("Rob", 10)
employee3 = Employee("Ron", 11)
employee4 = Employee("Von", 40)

print(employee1.name, employee1.get_salary())
print(employee2.name, employee2.get_salary())
print(employee3.name, employee3.get_salary())
print(employee4.name, employee4.get_salary())