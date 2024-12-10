from book import Book
from user import User
from library import Library


class Librarian(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def role_description(self):
        return f"{self.name} is a librarian."

    def add_book(self, library : Library, book: Book):
        library.add_book(book)
        print(f"Libraryian {self.name} added book {book.title} to the library")

    def remove_book(self, library: Library, book_title: str):
        removed = library.remove_book(book_title)

        if removed:
            print(f"Librarian {self.name} removed the book {book_title} from the library")

        else:
            print(f"Book '{book_title}' not found in the library")
