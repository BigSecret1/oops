from user import User
from book import Book


class Member(User):
    def __init__(self, user_id : int, name : str):
        super().__init__(user_id, name)

    def role_description(self):
        return f"{self.name} is library member."

    def borrow_book(self, book: Book):
        if book.get_copies_available() > 0:
            book.set_copies_available(book.get_copies_available() - 1)
            print(f"{self.name} borrowed book {book.title}")
        else:
            print(f"{book.title} is currently unavailable!")

    def return_book(self, book : Book):
        book.set_copies_available(book.get_copies_available() + 1)
        print(f"{self.name} returned {book.title}.")
