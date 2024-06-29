task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print(f"The task '{task}' is of high priority.")
    case "medium":
        print(f"The task '{task}' is of medium priority.")
    case "low":
        print(f"The task '{task}' is of low priority.")
    case _:
        print(f"The task '{task}' has an unknown priority level.")

if time_bound == "yes":
    print(" It requires immediate attention today!")

