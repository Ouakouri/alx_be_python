task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"The task '{task}' is of high priority."
    case "medium":
        reminder = f"The task '{task}' is of medium priority."
    case "low":
        reminder = f"The task '{task}' is of low priority."
    case _:
        reminder = f"The task '{task}' has an unknown priority level."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

print(reminder)
