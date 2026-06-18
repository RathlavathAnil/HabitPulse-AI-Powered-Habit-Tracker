from storage import save_habits


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