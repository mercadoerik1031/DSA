import os
import random


def get_random_questions() -> None:
    question_list = []

    for folder in os.listdir("./"):
        if folder[0].isnumeric():
            list_of_question = os.listdir(f"./{folder}")
            random_question = random.choice(list_of_question)
            question_list.append((folder, random_question))

    print()
    for i, question in enumerate(question_list):
        print(f"{i + 1}. Folder: {question[0]}, Question: {question[1]}")
    print()


def main():
    get_random_questions()


if __name__ == "__main__":
    main()
