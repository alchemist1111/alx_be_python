# Function to display the menu options to the user
def display_menu():
    print("\nShopping List Manager.")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
    
# Main function where the shopping list logic runs
def main():
    #   An empty shopping list
      shopping_list = []
      
    #   Loop continuously until the user decides to exit
      while True:
          display_menu() # Show menu options
          choice = input("Enter your choice: ") # Get the user input
          
          if choice == "1":
              # Handle adding an item
              item = input("Enter the item to add: ").strip()
              if item: # Check that the item is not empty
                  shopping_list.append(item) # Add the item to the list
                  print(f'"{item}" has been added to your shopping list.')
              else:
                  print("Item name cannot be empty.") # Warn if input is blank
                  
          elif choice == "2":
              # Handle removing an item
              item = input("Enter the item to remove: ").strip()
              if item in shopping_list:
                  shopping_list.remove(item) # Remove item if it exists
                  print(f'"{item}" has been removed from your shopping list.')
              else:
                  print(f'"{item}" not found in your shopping list.') # Throw an error if item not in the list
                  
          elif choice == "3":
              # Handle viewing the current shopping list
              if shopping_list:
                  print("\nYour Shopping List:")
                  # Display each item with its index starting from 1
                  for index, item in enumerate(shopping_list, start=1):
                      print(f"{index}. {item}")
              else:
                  print("Your shopping list is currently empty.")
                  
          elif choice == "4":
              # Exit the program
              print("Goodbye")
              break
          
          else:
              # Handle any invalid input
              print("Invalid choice. Please try again.")
              
if __name__ == "__main__":
    main()                                                        