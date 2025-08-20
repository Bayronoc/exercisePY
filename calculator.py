def add(a,b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def calculator():
    """Simple calculator function to perform basic arithmetic operations."""
    print("Welcome to the simple calculator!")
    print("Available operations: add, subtract, multiply, divide")
    while True:
        operation = input("Enter operation: ").strip().lower()
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'divide':
            result = divide(a, b)
        else:
            print("Invalid operation.")
            return
        
        print(f"The result is: {result}")

        print("Can you do another calculation? (yes/no)")
        answer = input().strip().lower()
        
        if answer != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Welcome to the simple calculator!")
            print("Available operations: add, subtract, multiply, divide")
            continue
    
calculator()