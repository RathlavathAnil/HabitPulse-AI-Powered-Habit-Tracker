from storage import load_habits
from habit_manager import (
    add_habit,
    update_progress,
    show_progress,
    delete_habit
)
from ai_coach import ask_ai


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