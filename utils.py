from constants import PLAY_AGAIN_PROMPT


def get_next_player_index(
    players: list[str],
    current_player_index: int = None,
) -> int:
    """
    Get the index of the next player in the players list.

    Args:
        players (list[str]): List of player names.
        current_player_index (int, optional): The current player's index. Defaults to None.

    Returns:
        int: The index of the next player.
    """
    if current_player_index == None:
        return 0
    return (current_player_index + 1) % len(players)


def choose_sticks(prompt: str, max_sticks: int) -> int:
    """
    Prompt the user to choose a number of sticks between 1 and 3.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        int: The number of sticks chosen by the player.
    """
    while True:
        try:
            sticks = int(input(prompt))
            if 1 <= sticks <= max_sticks:
                return sticks
            else:
                print(f"Please choose a number between 1 and {max_sticks}.")
        except ValueError:
            print(f"Invalid input. Please enter an integer between 1 and {max_sticks}.")


def play_again() -> bool:
    """Prompts the user to play again or exit the game."""
    while True:
        response = input(PLAY_AGAIN_PROMPT).strip().lower()
        if response == "yes":
            return True  # User wants to play again
        elif response == "no":
            return False  # User wants to choose a new level
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
