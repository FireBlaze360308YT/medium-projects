from difflib import get_close_matches
import json
from datetime import datetime


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.575)

    if matches:
        return matches[0]


def chat_bot(knowledge: dict):
    while True:
        user_input: str = input("You: ")
        best_match: str | None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            if best_match == "what time is it?":
                print(f"Bot: {get_time()}")
            else:
                print(f"Bot: {answer}")
        else:
            print("Bot: I do not understand...")


def get_time() -> str:
    return datetime.now().strftime("%d/%m/%Y   %H:%M:%S")


if __name__ == '__main__':
    with open("info.json", "r") as file:
        brain = json.load(file)
    chat_bot(knowledge=brain)
