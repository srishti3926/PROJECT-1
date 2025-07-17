
# Simple Calculator in Python

def simple_calculator():
    print("=== Simple Calculator ===")

    try:
        # Get input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        # Perform calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Invalid operation. Please use +, -, *, or /.")
            return

        # Display result
        print(f"The result of {num1} {operation} {num2} is {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
simple_calculator()
