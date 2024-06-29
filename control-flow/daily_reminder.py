task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        Reminder = f"The task '{task}' is of high priority."
    case "medium":
        Reminder = f"The task '{task}' is of medium priority."
    case "low":
        Reminder = f"The task '{task}' is of low priority."
    case _:
        Reminder = f"The task '{task}' has an unknown priority level."

if time_bound == "yes":
    Reminder += " It requires immediate attention today!"

print(f"Reminder:", Reminder)
