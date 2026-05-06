class Book:
    library_name = "Central Library"

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name
    
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available



