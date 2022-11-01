
DIFFICULTY_RANGES = [3, 5, 10]


def get_difficulty() -> int:

    difficulty = -1
    while difficulty < 0:
        choice = input("Choose a difficulty, (E)asy, (M)edium, (H)ard: ").lower()

        if choice == "e":
            difficulty = 0
        elif choice == "m":
            difficulty = 1
        elif choice == "h":
            difficulty = 2
        else:
            print(f"Invalid difficulty choice ({choice}) must be one of e, m or h")

    return difficulty
