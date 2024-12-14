from product import Product
from typing import List


class PurchaseSection:
    def __init__(self, user_id : int):
        self.user_id : int = user_id
        self.products : List[Product] = []

    def display_all_products(self):
        for product in self.products:
            print(f"Name : {product.name} Price : {product.price} Quantity : {product.quantity}")

    def update_product_stock(self, product_id : int, reduce_quantity : int):
        for product in self.products:
            if product.id == product_id:
                product.quantity = max(product.quantity - reduce_quantity, 0)
                print(f"Product quantity has been reduced by {reduce_quantity}")
