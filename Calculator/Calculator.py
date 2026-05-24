def calculate_equation():
    print("Enter a mathematical equation (e.g., 2 + 3 * 4 - 5).")
    print("Type 'q' to quit.\n")

    while True:
        equation = input("Enter equation: ")

        if equation.lower() == 'q':  # Exit condition
            print("Exiting the calculator. Goodbye!")
            break

        try:
            # Using eval to calculate the result
            result = eval(equation)
            print(f"Result: {result}\n")

        except (SyntaxError, NameError):
            print("Error: Invalid equation! Please try again.\n")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed!\n")

if __name__ == "__main__":
    calculate_equation()
