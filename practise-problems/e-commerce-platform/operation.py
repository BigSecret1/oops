from product import Product
from user import User
from order import Order
from purchase_section import PurchaseSection


product1 = Product(432, "Diary", 41234.34, 24)
product2 = Product(232, "Iphone13", 4123434.34, 19)
product3 = Product(3343,"Headphones",150.0, 30)

purchase_section = PurchaseSection()
purchase_section.add_products_in_browsing_section(product1)
purchase_section.add_products_in_browsing_section(product2)
purchase_section.add_products_in_browsing_section(product3)

purchase_section.display_all_products()

user = User(101,"John Doe","john@example.com")

user.cart.add_product(product1, 12)
user.cart.add_product(product2, 11)

user.cart.display_items()

order = Order(user)
order.place_order()

# Shopping by user2
user2 = User(11,"Alice Doe","Alice@example.com")

user2.cart.display_items()


user2.cart.add_product(product1, 12)
user2.cart.add_product(product3, 2)

user2.cart.display_items()

order = Order(user2)
order.place_order()

user2.cart.display_items()


