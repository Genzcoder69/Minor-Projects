class coffee:
    # initialize coffee with name and price
    def __init__(self,name,price):
        self.name = name
        self.price = price

class order:
    # initialize order with empty list
    def __init__(self):
        self.items = []

    # now add coffee to order
    def add_item(self,coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    # now calculate total price
    def total(self):
        return sum(item.price for item in self.items)

    # show order summary
    def show_order(self):
        if not  self.items:
            print("No items in order>>")
            return
        print("\nYour order:")
        
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ₹{item.price}")
        print(f"Total: ₹{self.total()}\n")

    # handle checkout process
    def checkout(self):
        if not self.items:
            print("Your cart is empty!")
            return
        self.show_order()
        
        confirm = input("Proceed to checkout? (Yes/No): ").strip().lower()
        if(confirm == 'yes'):
            print("Order confirmed! Thank You.")
            self.items.clear()
        else:
            print("Checkout cancelled.")

# Display menu and handle user input
def main():
    menu = [
        coffee("Espresso", 200),
        coffee("Latte" , 350),
        coffee("Cappuccino" , 240),
        coffee("Americano" ,  190)
    ]
    a = order()

    # User interaction 
    while True:
        print("\n --- Coffee Name ---")
        for i, c in enumerate(menu,1):
            print(f"{i}.{c.name} - ₹{c.price}")
        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter an option:")
        if choice in ['1', '2', '3', '4']:
            a.add_item(menu[int(choice) - 1])
        elif choice == '5':
            a.show_order()
        elif choice == '6':
            a.checkout()
        elif choice == '7':
            print("Thaks for visiting! >< Goodbye ><")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
