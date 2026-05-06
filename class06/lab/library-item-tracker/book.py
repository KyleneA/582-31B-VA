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



