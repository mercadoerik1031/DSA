import os
import random


def get_random_questions() -> list:
    links = []

    # Step 1: Collect folders starting with a number and select random files
    folder_list = [
        os.path.join(".", item) for item in os.listdir(".") if item[0].isnumeric()
    ]

    # Step 2: Randomly select one file from each folder
    questions_folder = [
        os.path.join(folder, random.choice(os.listdir(folder)))
        for folder in folder_list
        if os.path.isdir(folder)
    ]

    # Step 3: Collect Python files, skipping test or cache files
    all_questions = [
        os.path.join(folder, file)
        for folder in questions_folder
        if os.path.isdir(folder)
        for file in os.listdir(folder)
        if file.endswith(".py") and "test" not in file and "cache" not in file
    ]

    # Step 4: Extract the second line or mark as missing
    for question in all_questions:
        with open(question, "r") as file:
            file.readline()  # Skip the first line
            second_line = file.readline().strip()
            links.append(second_line if second_line else "Missing Link")

    return links


def main():
    links = get_random_questions()

    for link in links:
        print(link)


if __name__ == "__main__":
    main()
