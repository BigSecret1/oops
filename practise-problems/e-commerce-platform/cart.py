from product import Product
from typing import List, Dict


class Cart:
    def __init__(self):
        self.__items : Dict[int, Dict[Product, int]] = {}

    @property
    def items(self):
        return self.__items

    def add_product(self, product : Product, quantity : int):
        if product.is_available(quantity):
            if product.id in self.__items:
                self.__items[product.id]['quantity'] = quantity
            else:
                self.__items[product.id] = {'product': product, 'quantity': quantity}
            print(f"{product.name} added in cart, Quantity : {quantity}")
        else:
            raise ValueError(f"Product {product.name} is out of the stock")

    def remove_product(self, product_id : int):
        if product_id in self.__items:
            del self.__items[product_id]
        else:
            raise ValueError("Product not in cart.")

    def display_items(self):
        if not self.__items:
            print("Cart is empty")
        else:
            print("Cart items")
            for item in self.__items.values():
                product : Product = item['product']
                quantity : int = item['quantity']
                print(f"Name : {product.name} Quantity: {quantity} Price : ${product.price * quantity}")

    def cart_total_price(self):
        total_amount : float = 0
        for item in self.items.values():
            product : Product = item['product']
            quantity : int = item['quantity']
            total_amount += (product.price * quantity)

        print(f"Total car price is : {total_amount}")
        return total_amount

    def clear_cart(self):
        self.__items.clear()