# Alpha Vending Machine

A command-line vending machine simulator written in Python.

---

## 1. Problem Statement

Selling small items like snacks and drinks by hand needs a person to be present, calculate the bill and update the stock. This is slow and error-prone: totals can be wrong, and items that are already sold out can still be offered.

The problem is to build a program that behaves like a vending machine. It should show the available products with their prices and stock, let a customer buy one or many items, verify the payment, update the stock after every sale and print a bill, all without manual work.

---

## 2. Scope of the Project

### In Scope

- Storing products with code, name, price and stock
- Displaying all items with their price and current stock
- Buying a single item by entering its code
- Buying multiple items with quantities and paying one combined total
- Validating item codes, quantities and stock availability
- Accepting exact payment only (less or more money is rejected)
- Updating stock after a successful purchase
- Printing a bill after payment
- Running in the console through a simple menu

### Out of Scope

- Returning change or accepting extra money
- Real payment methods such as UPI, cards or coins
- Graphical user interface
- Permanent data storage (stock resets when the program restarts)
- Admin features such as restocking and sales reports

---

## 3. Target Users

- **Customers (end users):** people who want to quickly view products and buy snacks or drinks from the machine
- **Python beginners and students:** learners who want a simple project showing how dictionaries, functions, loops and conditions work together
- **Teachers and evaluators:** people reviewing a beginner-level project built with core Python concepts
- **Future developers:** anyone who wants to extend the project with features like change, an admin mode or a GUI

---

## 4. High-Level Features

| Feature | Description |
|---------|-------------|
| Display items | Shows every product with its code, price and remaining stock |
| Single item purchase | Buy one item by entering its code and paying the exact price |
| Multiple item purchase | Add several items with quantities and check out with one total bill |
| Stock management | Stock reduces after each sale; out-of-stock items cannot be bought |
| Input validation | Rejects invalid item codes, zero or negative quantities and quantities above stock |
| Exact payment check | Accepts payment only if it matches the price or total |
| Billing | Prints a receipt with item details and amount paid after a successful payment |
| Menu-driven interface | Simple console menu that keeps running until the user exits |

---

Author: MIHIR
GitHub: [@MIHIR-26BCE10275](https://github.com/MIHIR-26BCE10275)
