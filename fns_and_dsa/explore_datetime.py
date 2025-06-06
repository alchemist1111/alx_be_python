from datetime import datetime, timedelta

# Function to display current date
def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

print(display_current_datetime())


# Function to calculate a future date after adding given number of days
def calculate_future_date(days):
    current_date = datetime.now() # Get today's date and time
    future_date = current_date + timedelta(days=days) # Add days
    return future_date.strftime("%Y-%m-%d") # Format as "YYYY-MM-DD"


def main():
    try:
        # Prompt user for number of days
        user_input = int(input("Enter the number of days to add to the current date: "))
        # Call function and display result
        future = calculate_future_date(user_input)
        print("Future date:", future)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        
if __name__ == "__main__":
    main()            