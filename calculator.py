from art import logo  # Import a visual logo

# Define basic arithmetic operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2  # Warning: division by zero is handled later

# Dictionary to map operation symbols to corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Perform a calculation and display the result
def calc(operation, n1, n2):
    result = operations[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {result}")
    return result

# Main calculator loop
def math_calc():
    print(logo)  # Show logo/art at the top
    num1 = float(input("What's your first number?: "))
    result = num1
    continue_calc = True

    while continue_calc:
        # Display available operations
        print("\nThe available Operations:")
        for symbol in operations:
            print(symbol)

        # Get a valid operation from the user
        while True:
            operation = input("Pick an Operation: ")
            if operation == "":
                print("You didn't add an operation.")
            elif operation not in operations:
                print("Invalid operation. Try again.")
            else:
                break

        # Get a valid second number (avoid division by zero)
        while True:
            num2 = float(input("What's the next number?: "))
            if operation == "/" and num2 == 0:
                print("Error. Division by zero is not allowed. Try another number.")
            else:
                break

        # Perform calculation and update result
        result = calc(operation, result, num2)

        # Ask the user whether to continue or start over
        choice_calc = input(
            f"Type 'y' to continue calculating with {result}, "
            "or type 'n' to start a new calculation, "
            "or type 'exit' to end the program:\n"
        ).lower()

        if choice_calc == "n":
            math_calc()  # Restart from beginning
            return
        elif choice_calc == "exit":
            continue_calc = False

# Start the calculator
math_calc()
