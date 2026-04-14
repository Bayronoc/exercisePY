from pedidos import ARCHIVO_HISTORY

def view_history():
    print("Order history:")
    try:
        with open(ARCHIVO_HISTORY, "r") as hf:
            history = hf.readlines()
            if history:
                for i, history in enumerate(history, start=1):
                    print(str(i) + ". " + history.strip())
            else:
                print("No orders have been made yet.")
    except FileNotFoundError:
        print("No order history found.")