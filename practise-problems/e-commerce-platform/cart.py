from product import Product
from typing import List


class Cart:
    def __init__(self, user_id : int):
        self.user_id : int = user_id
        self.items : List[Product] = []

    def add_product(self, product : Product):
        if product.quantity > 0:
            self.items.append(product)
            print("Item has been added to the cart!!!")
        else:
            print("Item is out of stock")

    def remove_product(self, item : Product):
        self.items.remove(item)
        print("Item has been removed from the cart")

    def display_items(self):
        for item in self.items:
            print(f"Name : {item.name} Quantity : {item.quantity} Price : {item.price}")

    def cart_total_price(self):
        total_amount : float = 0
        for item in self.items:
            total_amount += item.price
        print(f"Total car price is : {total_amount}")