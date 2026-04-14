# This file contains the menu options for the cafeteria.
ARCHIVO_HISTORY = "history.txt"


def order_cafe():
    print("Option to order cafe selected.")
    # Show the menu and take the order
    print("Menu:")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    choice = input("Please enter your choice: ")

    cafe_options = {
        '1': 'Espresso',
        '2': 'Latte',
        '3': 'Cappuccino'
    }

    if choice in cafe_options:
        print(f"You have ordered a {cafe_options[choice]}.")
        # Here you would add the order to the history
        with open(ARCHIVO_HISTORY, "a") as hf:
            hf.write(cafe_options[choice] + "\n")
    else:        
        print("Invalid choice. Please try again.")
