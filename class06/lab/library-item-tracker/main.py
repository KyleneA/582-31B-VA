from book import Book

book1 = Book("Kitchen", "Banana Yoshimoto", True)
book2 = Book("Cat's Cradle", "Kurt Vonnegut", False)

print(f"book 1: {book1.title} by {book1.author}. Available: {book1.available}")
print(f"book 2: {book2.title} by {book2.author}. Available: {book2.available}")

print()

# Testing Instance Methods
# should print error msg
book1.return_book()
book2.borrow()

# should not return error
book1.borrow()
book1.display_info()
book2.return_book()
book2.display_info()

print()

# Testing Class Method
print(Book.library_name)
Book.change_library_name("Montreal Central Library")
print(Book.library_name)
Book.show_count()

# Testing Static Method
title1 = Book.is_valid_title("")
title2 = Book.is_valid_title("O")
print(f"title1 is valid: {title1}; title2 is valid: {title2}")

print()

# Testing from_string method
string = "Clean Code,Robert C. Martin,True"
book3 = Book.from_string(string)
book3.display_info()