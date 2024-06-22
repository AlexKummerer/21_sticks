import random

STICKS = 21


GAME_TITLE = "Welcome to the Game 21 Sticks"
PLAYER_1 = "Player 1"
PLAYER_2 = "Player 2"
COMPUTER_NAME = "COMPUTER"
PLAY_AGAIN_PROMPT = "Do you want to play again? (yes/no): "
GOODBYE_MESSAGE = "Thanks for playing! Goodbye."


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


def computer_choice(sticks_pile: int, optimal_move_probability: float) -> int:
    """
    Computer's move based on the given probability of making an optimal move.

    Args:
        sticks_pile (int): The number of sticks remaining in the pile.
        optimal_move_probability (float): The probability (0 to 1) of making an optimal move.

    Returns:
        int: The number of sticks the computer chooses to take.
    """
    if random.random() < optimal_move_probability:
        if sticks_pile % 4 == 0:
            return random.randint(1, min(3, sticks_pile))
        else:
            return sticks_pile % 4
    else:
        return random.randint(1,min(3, sticks_pile))


def setup_game(mode: int) -> tuple[list[str], int]:
    """
    Setup the game by getting player names and deciding the starting player.

    Args:
        mode (int): Game mode (1 for two-player, 2 for player vs computer).

    Returns:
        tuple: List of player names and the index of the starting player.
    """
    if mode == 1:
        player1_name = input("Enter the name of Player 1: ")
        player2_name = input("Enter the name of Player 2: ")
        players = [player1_name, player2_name]
    elif mode == 2:
        player_name = input("Enter the name of Player 1: ")
        computer_name = COMPUTER_NAME
        players = [computer_name, player_name]

    return players, 0



def play_game(
    players: list[str], player_starting_index: int, computer_choice_function=None
):

    current_player_index = player_starting_index
    sticks_pile = STICKS

    print(f"{sticks_pile} sticks in the pile.")
    while sticks_pile > 0:
        player = players[current_player_index]
        print(f"\n{player}'s turn.")

        if computer_choice_function and player == COMPUTER_NAME:
            player_choice = computer_choice_function(sticks_pile)
            print(f"Computer takes: {player_choice} sticks.")

        else:
            max_sticks = min(3, sticks_pile)
            player_choice = choose_sticks(
                prompt=f"{player}, how many sticks do you take (1-{max_sticks})? ",
                max_sticks=max_sticks,
            )
        sticks_pile -= player_choice

        if sticks_pile <= 0:
            print(
                f"\n{player} took the last stick. {player} wins!"
            )
            break

        print(f"\n{sticks_pile} sticks remaining in the pile.")

        current_player_index = get_next_player_index(players, current_player_index)


def main():

    print(GAME_TITLE)
    while True:
        mode = int(input("Choose game mode:(1) Two players , (2) Player vs Computer: "))
        players, starting_player_index = setup_game(mode)
        if mode == 1:
            play_game(players, starting_player_index)

        if mode == 2:
            difficulty = (
                input(
                    "Choose computer difficulty: (easy, medium-easy, medium, medium-hard, hard): "
                )
                .strip()
                .lower()
            )
            difficulty_map = {
                "easy": lambda sticks_pile: computer_choice(
                    sticks_pile, 0.0
                ),  # 0% optimal moves
                "medium-easy": lambda sticks_pile: computer_choice(
                    sticks_pile, 0.25
                ),  # 25% optimal moves
                "medium": lambda sticks_pile: computer_choice(
                    sticks_pile, 0.50
                ),  # 50% optimal moves
                "medium-hard": lambda sticks_pile: computer_choice(
                    sticks_pile, 0.75
                ),  # 75% optimal moves
                "hard": lambda sticks_pile: computer_choice(
                    sticks_pile, 1.0
                ),  # 100% optimal moves
            }
            computer_choice_function = difficulty_map.get(
                difficulty, lambda sticks_pile: computer_choice(sticks_pile, 0.0)
            )
            play_game(players, starting_player_index, computer_choice_function)
        else:
            print("Invalid choice. Please restart the game and choose a valid mode.")

        if not play_again():
            print(GOODBYE_MESSAGE)
            break


if __name__ == "__main__":
    main()
