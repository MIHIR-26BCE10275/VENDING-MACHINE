# Alpha Vending Machine

A simple command-line vending machine simulator written in Python. Browse the available snacks and drinks, buy a single item, or build a cart of multiple items and pay in one go, just like a real vending machine.

---

## Features

- **Display items**: view every product with its code, price and current stock
- **Buy a single item**: pick an item by code and pay for it
- **Buy multiple items**: add several items with quantities, then check out with one total bill
- **Live stock tracking**: stock reduces after every purchase, and out-of-stock items can't be bought
- **Exact payment only**: the machine rejects both too little and too much money
- **Input checks**: invalid item codes, zero or negative quantities and quantities above stock are handled
- **Billing summary**: prints a receipt after a successful payment
---

## Available Items

| Code | Item    | Price (Rs.) | Initial Stock |
|------|---------|-------------|---------------|
| 1    | Chips   | 20          | 10            |
| 2    | Chocos  | 30          | 10            |
| 3    | Coke    | 50          | 9             |
| 4    | Cookies | 25          | 8             |
| 5    | Water   | 15          | 20            |
| 6    | Namkeen | 50          | 8             |

Items are stored in a dictionary in the format `code: ["name", price, stock]`, so it's easy to add or edit products.

---

##  Getting Started

### Prerequisites

- Python 3.6 or higher (uses f-strings)

### Installation and Run

```bash
# 1. Clone the repository
git clone https://github.com/MIHIR-26BCE10275/VENDING-MACHINE.git

# 2. Move into the project folder
cd VENDING-MACHINE

# 3. Run the program
python "ALPHA VENDING MACHINE.py"
```


---

##  How to Use

When the program starts, you'll see this menu:

```
1. Display Items
2. Buy Items
3. Buy Multiple Items
4. Exit
```

### 1. Display Items
Shows the list of all items with price and remaining stock.

### 2. Buy Items (single item)
1. Enter the **item code**
2. The machine shows the item name and price
3. Enter the **exact amount** to pay
4. On success, stock reduces by 1 and a receipt is printed

### 3. Buy Multiple Items
1. Enter an **item code**
2. Enter the **quantity**
3. Repeat for as many items as you like
4. Enter **`0`** as the item code to check out
5. Pay the **exact total** to receive your bill

### 4. Exit
Closes the program.

---

##  Sample Output

```
    __ALPHA VENDING MACHINE__
Code    Item            Price   Stock
1       Chips           rs.20   10
2       Chocos          rs.30   10
3       Coke            rs.50   9
4       Cookies         rs.25   8
5       Water           rs.15   20
6       Namkeen         rs.50   8

Enter item code: 1
 You selected: Chips
 Price: Rs.20
Pay Money: Rs.20

___PAYMENT SUCCESSFUL___
Item: Chips
Price: RS.20
Paid: RS.20
THANK YOU FOR PURCHASING
VISIT AGAIN
```

---

##  Concepts Used

- Dictionaries and lists
- Functions
- Loops (`while`, `for`)
- Conditional statements
- User input and formatted output (f-strings)

---

##  Future Improvements

- [ ] Accept extra money and return change
- [ ] Handle non-numeric input without crashing (`try`/`except`)
- [ ] Show per-item quantities in the multi-item bill
- [ ] Refund/restore stock if payment fails during checkout
- [ ] Admin mode to restock items and view sales
- [ ] Save stock and sales data to a file
- [ ] Add a GUI using Tkinter

---

##  Contributing

Suggestions and improvements are welcome! Feel free to fork this repository and open a pull request.

---

##  Author

**MIHIR**
GitHub: [@MIHIR-26BCE10275](https://github.com/MIHIR-26BCE10275)

---


