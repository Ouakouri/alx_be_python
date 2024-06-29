task = input("Enter the task description: ")

priority = input("Enter the task priority (high, medium, low): ").lower()

time_bound = input("Is the task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Task: {task}\nPriority: High"
        if time_bound == "yes":
            reminder += " - This task requires immediate attention today!"
    case "medium":
        reminder = f"Task: {task}\nPriority: Medium"
        if time_bound == "yes":
            reminder += " - Consider working on this task soon."
    case "low":
        reminder = f"Task: {task}\nPriority: Low"
        if time_bound == "yes":
            reminder += " - You might want to schedule this task soon."
    case _:
        reminder = "Invalid priority. Please enter 'high', 'medium', or 'low'."

print(reminder)
