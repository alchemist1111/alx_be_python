# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to choose the type of operation to perform
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using a Match Case statement
match operation:
    case "+":
        add = num1 + num2
        print("The result is:", add)
    case "-":
        subtract = num1 - num2
        print("The result is:", subtract)
    case "*":
        multiply = num1 * num2
        print("The result is:", multiply)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:    
            divide = num1 / num2
            print("The result is:", divide) 
    case _:
        print("Invalid operation. Please choose one of the following: +, -, *, /.")               
            
    