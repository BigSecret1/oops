from product import Product
from cart import Cart


class Order:
    def __init__(self, user_id : int, cart : Cart):
        self.user_id : int = user_id
        self.cart : Cart = cart

    def place_order(self):
        total_purchase : float = 0
        print(f"Order has been placed successfully by {self.user_id}")

        #reduce quantity of purchased products

        for item in self.cart.items:
            print(f"Item : {item.name} Quantity : {item.quantity} Price : {item.price}")
            total_purchase += item.price
            self.cart.remove_product(item)
        print(f"Total purchase amount is : {total_purchase}")
