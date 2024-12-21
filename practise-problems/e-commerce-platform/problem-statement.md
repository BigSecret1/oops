# Problem Statement: E-Commerce Platform

You are tasked with designing a basic e-commerce platform using Object-Oriented Programming principles in Python. The system should allow users to browse products, add them to a cart, and place an order. Here's a detailed breakdown:

---

## Requirements:

### Products:

- Each product should have attributes like:
  - `product_id`
  - `name`
  - `price`
  - `stock`
- Implement methods to:
  - Check product availability.
  - Update stock after a purchase.

### User:

- A user should have attributes like:
  - `user_id`
  - `name`
  - `email`
- Users should be able to:
  - Browse products.
  - Add them to their cart.

### Cart:

- The cart should belong to a user.
- It should store the products added by the user along with their quantities.
- Implement methods to:
  - Add a product to the cart.
  - Remove a product from the cart.
  - Display the contents of the cart.
  - Calculate the total price of items in the cart.

### Order:

- An order should include:
  - The user who placed it.
  - Products purchased (with quantities).
  - Total price.
- After placing an order:
  - The stock of the products should be updated.
  - The cart should be emptied.
