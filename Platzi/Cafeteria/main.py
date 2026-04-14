# Cafeteria
from menu import mostrar_menu
from pedidos import order_cafe
from history import view_history

def main():
    while True:
        mostrar_menu()
        choice = input("Please enter your choice: ")
        
        if choice == '1':
            order_cafe()
        elif choice == '2':
            view_history()
        elif choice == '3':
            print("Thank you for visiting the cafeteria. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()