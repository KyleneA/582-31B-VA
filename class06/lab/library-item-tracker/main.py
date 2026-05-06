from book import Book

book1 = Book("Kitchen", "Banana Yoshimoto", True)
book2 = Book("Cat's Cradle", "Kurt Vonnegut", False)

print(f"book 1: {book1.title} by {book1.author}. Available: {book1.available}")
print(f"book 2: {book2.title} by {book2.author}. Available: {book2.available}")

print()

# should print error msg
book1.return_book()
book2.borrow()

# should not return error
book1.borrow()
book1.display_info()
book2.return_book()
book2.display_info()