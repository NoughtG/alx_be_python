# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = f"'{task}' is a {priority} priority task"

# Process priority using match case
match priority:
    case "high":
        reminder += ". Act on it promptly"
    case "medium":
        reminder += ". Plan to address it soon"
    case "low":
        reminder += ". Consider completing it when you have free time"
    case _:
        reminder = f"'{task}' has an invalid priority. Please use high, medium, or low"

# Modify reminder for time-bound tasks
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["high", "medium", "low"]:
    reminder += "."
else:
    reminder += "."

# Print the reminder
if priority in ["high", "medium", "low"]:
    print(f"Reminder: {reminder}")
else:
    print(f"Note: {reminder}")
