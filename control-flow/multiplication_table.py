# Ask the user to input a number for which they want to see the multiplication table
number = float(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table using the for loop
for i in range(1, 11):
    product = number * i
    
    # Show the multiplication table in the terminal
    print(f"{number} * {i} = {product}")