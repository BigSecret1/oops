from product import Product
from typing import List


class PurchaseSection:
    def __init__(self):
        self.__products : List[Product] = []

    def add_products_in_browsing_section(self, product : Product):
        self.__products.append(product)

    def display_all_products(self):
        for product in self.__products:
            print(f"Name : {product.name} Price : {product.price} Quantity : {product.quantity}")
