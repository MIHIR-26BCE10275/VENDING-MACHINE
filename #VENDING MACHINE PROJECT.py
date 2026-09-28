#VENDING MACHINE PROJECT 

items= {                                    #these are the things available in vending machine
    1:["Chips",20,10],
    2:["Chocos",30,10],
    3:["Coke",50,9],
    4:["Cookies",25,8],                     # ["name",price,stock]
    5:["Water",15,20],
    6:["Namkeen",50,8]
}

def display_items():                                         #with this we can check if the stock is available or we need to restock it.
    print("    __ALPHA VENDING MACHINE__") 

    print("Code\tItem\t\tPrice\tStock")

    for code, details in items.items():
        print(f"{code}\t{details[0]}\t\trs.{details[1]}\t{details[2]}")


    name=items[code][0]         #this gives the list of available things in vending machine with their MRP and stock.
    price=items[code][1]
    stock=items[code][2]    


def buy_items():
    code=int(input("\nEnter item code: "))
    if code not in items:
        print("Invalid Item Code")
        return                                           #this code is used when customer wants only 1 item.
    name=items[code][0]
    price=items[code][1]
    stock=items[code][2] 

    if stock==0:
        print("Currently this item is out of stock ")
        return
    print(f" You selected: {name}")
    print(f" Price: Rs.{price}")


    money=int(input("Pay Money: Rs."))          # customer has to pay accurate amount because machine would not accept less or more amount.
    if money<price:
        print(" Insufficient amount ")
        return
    if money>price:
        print("Please pay accurate amount")
        return

    items[code][2]-=1           

    print("\n___PAYMENT SUCCESSFUL___")        #this is the billing section.
    print(f"Item: {name}")
    print(f"Price: RS.{price}")
    print(f"Paid: RS.{money}")
    print("THANK YOU FOR PURCHASING")
    print("VISIT AGAIN")


def buy_multiple_items():           #this code is used when customer wants to buy multiple items.
    total=0
    selected_items=[]
    while True:
        display_items

        code=int(input(" Enter Item code: "))

        if code==0:                                 #enter 0 as input when you have selected all the products you want to get bill now 
            break
        if code not in items:
            print("Invalid Item Code") 
            continue

        quantity= int(input("Enter Quantity :"))
        print("ENTER 0 TO CHECKOUT")
        
        if quantity<=0:
            print("Quantity should be >=1")
            continue
        if quantity> items[code][2]:
            print("Insufficient stock")
            continue

        selected_items.append(items[code][0])        #this makes the list of selected items and is used in billing section.

        total +=(items[code][1]*quantity)               #this is the total amount which customer has to pay.
        
        items[code][2] -= quantity
    print("Pay Money :", total)
    money=int(input("Pay Money: Rs."))
    if money<total:
        print(" Insufficient amount ")
        return
    if money>total:
        print("Please pay accurate amount")
        return
    
    

    print(f"\n___PAYMENT SUCCESSFUL___")            #this is billing section.
    print("Items Purchased:")
    for name in selected_items:print(name)
    print(f"Price: RS.{total}")
    print(f"Quantity: {quantity}")
    print(f"Paid: RS.{money}")
    print("THANK YOU FOR PURCHASING")
    print("VISIT AGAIN")


def main():
    while True:
        print("\n1. Display Items")                     #because of this code we get on different interfaces when we enter different codes.
        print("2. Buy Items")
        print("3. Buy Multiple Items")
        print("4. Exit")

        choice=int(input("Enter Choice: "))

        if choice==1:
            display_items()
        elif choice==2:
            display_items()
            buy_items()
        elif choice==3:
            display_items()
            buy_multiple_items()
        elif choice==4:
            print("Please Visit Again")
            break
        else:
            print("Invalid Coice, Please Try Again")

    
main()