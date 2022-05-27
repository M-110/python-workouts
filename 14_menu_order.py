"""
In this exercise, I want you to create a new constant dict, called MENU, 
representing the possible items you can order at a restaurant. The keys will 
be strings, and the values will be prices (i.e., integers). You should then 
write a function, restaurant, that asks the user to enter an order:

-If the user enters the name of a dish on the menu, the program prints the 
price and the running total. It then asks the user again for their order.

-If the user enters the name of a dish not on the menu, the program scolds the 
user (mildly). It then asks the user again for their order.

-If the user enters an empty string, the program stops prompting and prints 
the total amount.
"""

MENU = {"sandwhich": 5,
        "tea": 3,
        "apple": 1,
        "rice": 12}

def order_food():
    total = 0
    while order := input('Order: '):
        if order in MENU:
            total += MENU[order]
            print(f'{order} costs {MENU[order]}, total is {total}.')
        else:
            print(f"Sorry, we don't have any {order}.")
    print(f"The total cost will be {total}.")

order_food()

