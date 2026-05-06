class Book:
    library_name = "Central Library"

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name

    @staticmethod
    def is_valid_title(title):
        if (len(title) > 0):
            return True
        return False

    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available
    
    def borrow(self):
        if (self.available):
            self.available = False
        else:
            print(f"{self.title} by {self.author} is not available to borrow")
    
    def return_book(self):
        if (self.available == False):
            self.available = True
        else:
            print(f"This copy of {self.title} by {self.author} does not belong to us")
    
    def display_info(self):
        print(f"'{self.title}' by {self.author}. Availability: {self.available}")
