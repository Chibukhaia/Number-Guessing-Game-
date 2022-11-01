import random
from players_number import *


def play_game(higher_number: int):

    computers_number = random.randint(1, higher_number)
    players_number = -1
    while players_number != computers_number:
        players_number = get_players_number(higher_number)

        if players_number > computers_number:
            print(f"{players_number} is  too high!")
        elif int(players_number) < computers_number:
            print(f"{players_number} is  too low!")
        else:
            print(f"Computer says: {computers_number}, you say: {players_number}")
            print("You won!")
