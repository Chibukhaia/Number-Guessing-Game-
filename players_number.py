
def get_players_number(higher_number: int) -> int:
    # The try block lets you test a block of code for errors.
    # The except block lets you handle the error.
    while True:
        players_number = input(f"Pick a number between 1-{higher_number}: ")
        try:
            players_number = int(players_number)
        except ValueError:
            print(f"Invalid number  ({players_number}), must be valid number")
            continue
        if 1 <= players_number <= higher_number:
            return players_number
        print(f"Invalid guess ({players_number}), must be between 1 and {higher_number}")

