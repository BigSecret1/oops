class Product:
    def __init__(self, id : int, name : str, price : float, stock: int):
        self.__id : int = id
        self.__name : str = name
        self.__price : float = price
        self.__stock : int = stock

    @property
    def id(self):
        return self.__id
    
    @property
    def stock(self):
        return self.__stock
    
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def is_available(self, quantity : int) -> bool:
        return self.__stock >= quantity

    def update_stock(self, quantity : int):
        if self.__stock >= quantity:
            self.__stock -= quantity
        else:
            raise ValueError("Insufficient stock at the moment.")