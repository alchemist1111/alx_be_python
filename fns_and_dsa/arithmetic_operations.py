# Function definition to perform operations
def perform_operation(num1: float, num2: float, operation: str):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Cannot divide by zero.")
            return None
        else:
            result = num1 / num2
    else:
        print("Invalid operation. Please choose one of the following: add, subtract, divide, multiply.")
        return None
        
    return result                           