from difficulty import *
from game import *


def main_rules():
    is_playing = True

    while is_playing:

        difficulty = get_difficulty()
        higher_number = DIFFICULTY_RANGES[difficulty]
        play_game(higher_number)

        while True:
            play_again = input("Do you want to play again? (Y/N): ").lower()

            if play_again == "n":
                is_playing = False
                print("Have a great day!")
                break

            if play_again == "y":
                break

            print(f"Invalid option ({play_again}), must be Y/N")


print((main_rules()))
