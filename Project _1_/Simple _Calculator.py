"""
PROJECT 1: SIMPLE CALCULATOR
Coding Samurai Internship - Level 1 (Beginner)
Author: Sharvari Thakur
Description: A simple calculator that performs basic arithmetic operations
"""

def add(x, y):
    """Function to add two numbers"""
    return x + y


def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y


def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y


def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    """Main calculator function"""
    print("\n" + "="*50)
    print("        SIMPLE CALCULATOR")
    print("="*50)
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("="*50)
    
    while True:
        # Take input from user
        choice = input("\nEnter choice (1/2/3/4/5): ")
        
        # Exit condition
        if choice == '5':
            print("\nThank you for using Calculator! Bye! 👋")
            break
        
        # Check if choice is valid
        if choice in ('1', '2', '3', '4'):
            try:
                # Take numbers from user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                # Perform calculation based on choice
                if choice == '1':
                    print(f"\n{num1} + {num2} = {add(num1, num2)}")
                
                elif choice == '2':
                    print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
                
                elif choice == '3':
                    print(f"\n{num1} × {num2} = {multiply(num1, num2)}")
                
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {result}")
            
            except ValueError:
                print("\nInvalid input! Please enter valid numbers.")
        
        else:
            print("\nInvalid choice! Please enter 1, 2, 3, 4, or 5.")


# Run the calculator
if __name__ == "__main__":
    calculator()