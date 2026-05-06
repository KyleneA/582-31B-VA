from book import Book

book1 = Book("Kitchen", "Banana Yoshimoto", True)
book2 = Book("Cat's Cradle", "Kurt Vonnegut", True)

print(f"book 1: {book1.title} by {book1.author}. Available: {book1.available}")
print(f"book 2: {book2.title} by {book2.author}. Available: {book2.available}")

print()

print(Book.library_name)
Book.change_library_name("Montreal Central Library")
print(Book.library_name)