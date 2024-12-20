from cart import Cart

class User:
    def __init__(self, id : int, name : str, email : str):
        self.__id : int = id
        self.__name : str = name
        self.__email : str = email
        self.cart = Cart(self)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__name

    def __str__(self):
        return f"User ID : {self.__id}, Name : {self.__name} Email : {self.__email}"
