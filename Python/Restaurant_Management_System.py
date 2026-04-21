''' --- Restaurant Management System ---'''

veg_menu = {
    'Pizza': 80,
    'Burger': 40,
    'Pasta': 30,
    'Salad': 10,
    'Coffee': 70,
    'Sandwich': 50,
    'Paneer Tikka': 120,
    'Veg Biryani': 140,
    'Masala Dosa': 60,
    'Idli Sambhar': 50,
    'Chole Bhature': 90,
    'Veg Fried Rice': 110,
    'Manchurian': 100,
    'Spring Rolls': 80,
    'French Fries': 60,
    'Cold Drink': 40,
    'Ice Cream': 50
}

non_veg_menu = {
    'Mutton Biryani': 220,
    'Chicken Biryani': 160,
    'Chicken Korma': 180,
    'Fish Curry': 200,
    'Butter Chicken': 210,
    'Chicken Tikka': 170,
    'Egg Curry': 90,
    'Fish Fry': 180,
    'Chicken Fried Rice': 150,
    'Prawn Curry': 250,
    'Mutton Curry': 230,
    'Chicken Lollipop': 140,
    'Grilled Chicken': 200,
    'Chicken Wings': 160,
    'Egg Bhurji': 70
}

print("--- WELCOME TO OUR RESTAURANT ---")
choice = input("What You want to choose (veg/non_veg)\n").lower()

if (choice == 'veg'):
    for item, price in veg_menu.items():
        print(f"{item}:{price}")
elif(choice == 'non_veg'):
    for item, price in non_veg_menu.items():
        print(f"{item}:{price}")
else:
    print("Invalid choice !")

total_order_amount = 0

item1 = input("Enter your order:>>>\n").title()
if (item1 in veg_menu):
    total_order_amount += veg_menu[item1]
    print(f"{item1} has been added to your order !")
elif (item1 in non_veg_menu):
    total_order_amount += non_veg_menu[item1]
    print(f"{item1} has been added to your order !")
else:
    print("Sorry!")
    print(f"{item1} not available ! ")

another_order = input("Want to add another item? (Yes/No)").lower()

if(another_order == 'yes'):
    item2 = input("Enter the name of second item :>>>").title()

    if(item2 in veg_menu):
        total_order_amount += veg_menu[item2]
        print(f"{item2} has been added to your order !")
    elif(item2 in non_veg_menu):
        total_order_amount += non_veg_menu[item2]
        print(f"Your item {item2} has been added to your order !")
    else:
        print(f"{item2} not available !")

print(f"Amount to be paid : {total_order_amount}")