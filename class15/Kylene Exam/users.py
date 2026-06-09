class User:
    @staticmethod
    def is_valid_input(input, min_length):
        clean_input = input.strip()
        input_length = len(clean_input)

        is_empty_input = clean_input == ""
        is_short_input = input_length < min_length

        return not (is_empty_input or is_short_input)

    def __init__(self, name, email):
        if not User.is_valid_input(name, 2):
            raise ValueError("Name must contain at least 2 letters.")
        else:
            self.__name = name
            self.email = email

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if not User.is_valid_input(value, 8):
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

