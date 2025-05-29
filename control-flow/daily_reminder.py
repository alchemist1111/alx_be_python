# Ask the user to input a task description and save it into a task variable
task = input("Enter your task: ")

# Prompt the user to enter the task priority
priority = input("Priority (high, medium, low): ").lower()

# Prompt the user to ask if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use Match Case to handle priority levels
match priority:
    case "high":
        reminder = f"{task} is a high priority task"
    case "medium":
        reminder = f"{task} is a medium priority task"
    case "low":
        reminder = f"{task} is a low priority task"
    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")
 
 # Modify reminder based on time sensitivity       
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
    print(f"Note: {reminder}")
else:
    print("Invalid input for time-bound. Please enter yes or no.")                         