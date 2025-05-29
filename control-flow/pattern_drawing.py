# Prompt the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop to handle rows
while row < size:
    # Inner for loop to print '*' for each column in the current row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after printing one row
    print()
    
    # Increment the row counter
    row += 1