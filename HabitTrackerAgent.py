import ollama
import json
import os

FILE_NAME = "habits.json"


# Load habits
def load_habits():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}


# Save habits
def save_habits(habits):
    with open(FILE_NAME, "w") as file:
        json.dump(habits, file, indent=4)


# Add habit
def add_habit(habits):
    habit_name = input("Habit Name: ").strip().lower()

    if habit_name in habits:
        print("Habit already exists!")
        return

    try:
        goal = int(input("Goal (number): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    habits[habit_name] = {
        "goal": goal,
        "progress": 0
    }

    save_habits(habits)
    print("Habit added successfully!")


# Update progress
def update_progress(habits):

    if not habits:
        print("No habits found.")
        return

    print("\nAvailable Habits:")
    for habit in habits:
        print("-", habit.title())

    habit_name = input("\nHabit Name: ").strip().lower()

    if habit_name not in habits:
        print("Habit not found.")
        return

    try:
        amount = int(input("Progress to add: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    habits[habit_name]["progress"] += amount

    save_habits(habits)
    print("Progress updated!")


# Show progress
def show_progress(habits):

    if not habits:
        print("No habits found.")
        return

    print("\n===== YOUR HABITS =====")

    for habit, details in habits.items():

        goal = details["goal"]
        progress = details["progress"]

        percentage = (progress / goal) * 100 if goal > 0 else 0

        print(
            f"{habit.title()} | "
            f"{progress}/{goal} | "
            f"{percentage:.1f}% Complete"
        )

    print()


# Delete habit
def delete_habit(habits):

    if not habits:
        print("No habits found.")
        return

    print("\nAvailable Habits:")
    for habit in habits:
        print("-", habit.title())

    habit_name = input("\nHabit to delete: ").strip().lower()

    if habit_name not in habits:
        print("Habit not found.")
        return

    del habits[habit_name]

    save_habits(habits)

    print("Habit deleted successfully!")


# AI Coach
def ask_ai(habits):

    user_input = input("Ask the AI Coach: ")

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": f"""
You are a friendly Habit Tracker AI Coach.

Responsibilities:
- Motivate the user.
- Suggest useful habits.
- Help improve consistency.
- Use the user's habit data.
- Keep answers short and practical.

Current habits:
{json.dumps(habits, indent=2)}
"""
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("\nAI Coach:")
    print(response["message"]["content"])
    print()


# Main Program
def main():

    habits = load_habits()

    print("===== HABIT TRACKER AI =====")

    while True:

        print("\nChoose an option")
        print("1. Add Habit")
        print("2. Update Progress")
        print("3. Show Progress")
        print("4. Ask AI Coach")
        print("5. Delete Habit")
        print("6. Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            add_habit(habits)

        elif choice == "2":
            update_progress(habits)

        elif choice == "3":
            show_progress(habits)

        elif choice == "4":
            ask_ai(habits)

        elif choice == "5":
            delete_habit(habits)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()