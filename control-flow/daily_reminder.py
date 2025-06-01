task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = f"Reminder: '{task}' is a {priority} priority task"

match priority:
    case "high":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Plan to address it soon."
    case "medium":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Schedule it for the near future."
    case "low":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Complete it when you have time."
    case _:
        reminder = "Invalid priority level. Please choose high, medium, or low."

print(reminder)
