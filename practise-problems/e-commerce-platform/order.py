from product import Product
from user import User


class Order(User):
    def __init__(self , user : User):
        self.__user = user
        self.products = []
        self.__total_price : float = 0

    def place_order(self):
        cart_items = self.__user.cart.items

        if not cart_items:
            raise ValueError("Cart is empty, add items to place an order"
                             )
        total_purchase : float = 0

        for item in self.cart.items.values():
            product : Product = item['product']
            quantity : int = item['quantity']

            product.update_stock(quantity)

            self.products.append((product, quantity))

            self.__total_price = self.__user.cart.cart_total_price()
            self.__user.cart.clear_car()

            print("Order placed successfully")
            self.display_order_details()

    def display_order_details(self):
        print(
            "\nOrder Summary:")
        print(
            f"Customer: {self.__user.name}")
        for product, quantity in self.__products:
            print(
                f"{product.name} - Quantity: {quantity}, Price: ${product.price * quantity}")
        print(
            f"Total Price: ${self.__total_price}")