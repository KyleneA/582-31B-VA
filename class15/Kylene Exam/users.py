from helperMethods import HelperMethods

class User:
    def __init__(self, name, email):
        if not HelperMethods.is_valid_input(name, 2):
            raise ValueError("Name must contain at least 2 letters.")
        else:
            self.__name = name
            self.email = email

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if not HelperMethods.is_valid_input(value, 8):
            raise ValueError("Email must contain more than 8 characters.")
        elif not "@" in value:
            raise ValueError("Email must contain an '@ symbol'")
        else:
            self.__email = value
    
    def display_info(self):
        return f"Name: {self.__name} | Email: {self.email}"

class Customer(User):
    number_of_customers = 0

    @classmethod
    def add_customer(cls):
        cls.number_of_customers += 1
        return cls.number_of_customers

    def __init__(self, name, email):
        super().__init__(name, email)
        self.__customer_id = Customer.add_customer()
    
    def display_info(self):
        customer_user_info = super().display_info()
        return f"| CUSTOMER | Customer ID: {self.__customer_id} | {customer_user_info}"

class VIPCustomer(Customer):
    def __init__(self, name, email):
        super().__init__(name, email)
    
    def display_info(self):
        VIP_info = super().display_info()
        return f"** VIP ** {VIP_info}"

class Staff(User):
    number_of_employees = 0

    @classmethod
    def add_employee(cls):
        cls.number_of_employees += 1
        return cls.number_of_employees

    def __init__(self, name, email):
        super().__init__(name, email)
        self.__employee_id = Staff.add_employee()
    
    def display_info(self):
        employee_user_info = super().display_info()
        return f"| STAFF | Employee ID: {self.__employee_id} | {employee_user_info}"