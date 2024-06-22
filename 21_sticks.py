from constants import GAME_TITLE, GOODBYE_MESSAGE, DIFFICULTY_CONFIG
from utils import play_again
from game import setup_game, play_game
from computer_strategies import get_computer_choice_function


def main_menu() -> int:
    """
    Display the main menu and get the game mode selection from the user.

    Returns:
        int: The selected game mode (1 for two players, 2 for player vs computer).
    """
    while True:
        try:
            mode = int(
                input("Choose game mode: (1) Two Players, (2) Player vs Computer: ")
            )
            if mode in [1, 2]:
                return mode
            else:
                print("Invalid choice. Please choose 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def select_computer_difficulty() -> callable:
    """
    Prompt the user to select the computer's difficulty level and return the corresponding strategy function.

    Returns:
        callable: The function to use for the computer's move based on the selected difficulty.
    """
    # Create a prompt string with user-friendly difficulty descriptions
    difficulty_prompt = (
        "Choose computer difficulty: ("
        + ", ".join([config["description"] for config in DIFFICULTY_CONFIG.values()])
        + "): "
    )

    while True:
        difficulty_input = input(difficulty_prompt).strip().lower()

        # Map the user-friendly input to the internal difficulty key
        difficulty_key = next(
            (
                key
                for key, config in DIFFICULTY_CONFIG.items()
                if config["description"].lower() == difficulty_input
            ),
            None,
        )

        if difficulty_key:
            return get_computer_choice_function(difficulty_key)
        else:
            print("Invalid choice. Please choose a valid difficulty level.")


def main():
    """
    Main function to start the game.
    """
    print(GAME_TITLE)
    while True:
        mode = main_menu()

        players, starting_player_index = setup_game(mode)

        if mode == 1:
            play_game(players, starting_player_index)
        else:
            computer_choice_function = select_computer_difficulty()
            play_game(players, starting_player_index, computer_choice_function)

        if not play_again():
            print(GOODBYE_MESSAGE)
            break


if __name__ == "__main__":
    main()
