from datetime import datetime

# Function to display current date
def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

print(display_current_datetime())