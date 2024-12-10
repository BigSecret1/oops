import book

class Library:
    def __init__(self):
        self.books : book = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title: str):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return True
        return False

    def display_books(self):
        if not self.books:
            print("Library is empty sorry...")
        else:
            print("Books in the library :")
            for book in self.books:
                book.display_details()