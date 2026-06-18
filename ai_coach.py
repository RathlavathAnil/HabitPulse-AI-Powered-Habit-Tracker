import ollama
import json


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