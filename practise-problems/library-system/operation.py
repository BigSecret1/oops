from librarian import Librarian
from library import Library
from book import Book
from member import Member


# Create a Library
library = Library()

# Create Books
book1 = Book("1984", "George Orwell", "1234567890", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321", 3)

# Create Users
librarian = Librarian(1, "Alice")
member = Member(2, "Bob")

# Librarian adds books to the library
librarian.add_book(library, book1)
librarian.add_book(library, book2)

# Display available books
library.display_books()

# Member borrows a book
member.borrow_book(book1)
member.borrow_book(book2)

# Display books after borrowing
library.display_books()

# Member returns a book
member.return_book(book1)

# Display books after returning
library.display_books()

# Librarian removes a book
librarian.remove_book(library, "1984")

# Display books after removal
library.display_books()
