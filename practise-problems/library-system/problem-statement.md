# Library Management System

## Problem Statement
You are tasked with designing a Library Management System using Object-Oriented Programming (OOP) concepts in Python. The system should manage books, users, and borrowing operations. Use abstraction, encapsulation, inheritance, and polymorphism to implement the solution.

## Requirements

### Books

Each book has:
- `title`
- `author`
- `ISBN`
- `copies_available`

**Features:**
- Implement a way to display book details.
- Update the number of available copies.

### Users

There are two types of users:
1. **Member**: Can borrow books.
2. **Librarian**: Can add or remove books.

**Common attributes for all users:**
- `user_id`
- `name`

**Polymorphism:**
- Define roles and actions for `Member` and `Librarian`.

### Borrowing Operations

A member can:
- Borrow a book if copies are available.
- Return a book to increase available copies.
- If no copies are available, the system should notify the user.

### Concepts to Use

#### Encapsulation
- Protect attributes like `copies_available` to prevent direct modification.
- Use getters and setters to manage access to sensitive data.

#### Abstraction
- Define an abstract class `User` that enforces a `role_description` method for all user types.
