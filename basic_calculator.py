def basic_calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")

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
                    result = "Error! Division by zero."
            else:
                result = "Invalid operation!"

            print(f"The result is: {result}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != 'yes':
            break

basic_calculator()
