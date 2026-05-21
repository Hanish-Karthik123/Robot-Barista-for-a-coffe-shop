#Robot Coffee Shop Waiter
#This program simulates a robot waiter taking orders at a coffee shop. The user can select a drink from the menu, and the program will provide feedback on the selection and the price. The user can also select a payment method, and the program will confirm the selection.
print("Welcome to Planetbucks")

#Customer interaction
customer_name = str(input("What is your name? "))
print(f"Hello {customer_name}, welcome to Planetbucks! We have a variety of drinks to choose from.")
print("Here is our menu:")
menu = ["Coffee", "Tea", "Juice", "Smoothie", "Water", "Milkshake"]
print(menu)
user_selection = str(input("Please select a drink from the menu: ")).lower()

#Check if the user's selection is valid and provide feedback
if user_selection in [item.lower() for item in menu]:
    print(f"Great choice, {customer_name}! Your {user_selection} will be ready shortly.")
else:
    print(f"Sorry, {customer_name}, we don't have {user_selection} on the menu. Please select a drink from the menu.")
price = [250, 200, 150, 300, 100, 350]
if user_selection == "coffee":
    print(f"The price of your {user_selection} is {price[0]} ₹.")
elif user_selection == "tea":
    print(f"The price of your {user_selection} is {price[1]} ₹.")
elif user_selection == "juice":
    print(f"The price of your {user_selection} is {price[2]} ₹.")
elif user_selection == "smoothie":
    print(f"The price of your {user_selection} is {price[3]} ₹.")
elif user_selection == "water":
    print(f"The price of your {user_selection} is {price[4]} ₹.")
elif user_selection == "milkshake":
    print(f"The price of your {user_selection} is {price[5]} ₹.")
print("Thank you for your order! We hope you enjoy your drink.")

#Payment method selection
payment_method = str(input("Please select a payment method (cash, card, mobile payment): ")).lower()
if payment_method in ["cash", "card", "mobile payment"]:
    print(f"Thank you for choosing {payment_method} as your payment method. Your order will be processed shortly.")
    print(f"The payment of {price[menu.index(user_selection)]} ₹ has been processed successfully.")
    print("Thank you for visiting Planetbucks! We hope to see you again soon.")
else:
    print("Sorry, we don't accept that payment method. Please select a valid payment method.")