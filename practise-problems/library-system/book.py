class Book:
    def __init__(self, title : str, author : str, isbn : int, copies_available : int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__copies_available = copies_available

    def get_copies_available(self):
        return self.__copies_available

    def set_copies_available(self, count: int):
        if count >= 0:
            self.__copies_available = count
        else:
            raise ValueError("Copies available can't be negative")

    def display_details(self):
        print(f"Title : {self.title} Author : {self.author} ISBN : {self.isbn} Available Copies : {self.__copies_available}")
