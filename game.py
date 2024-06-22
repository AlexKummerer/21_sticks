from constants import STICKS, COMPUTER_NAME
from utils import get_next_player_index, choose_sticks
import random


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
        player_name = input("Enter your name: ")
        players = [COMPUTER_NAME, player_name]

    starting_player_index = random.randint(0, 1)  # Randomly choose the starting player
    return players, starting_player_index


def handle_player_turn(
    player: str, sticks_pile: int, computer_choice_function=None
) -> int:
    """
    Handle the actions for a player's turn.

    Args:
        player (str): The name of the current player.
        sticks_pile (int): The number of sticks remaining in the pile.
        computer_choice_function (callable, optional): Function to determine the computer's move. Defaults to None.

    Returns:
        int: The number of sticks chosen by the player.
    """
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

    return player_choice


def determine_winner(player: str):
    """
    Announce the winner of the game.

    Args:
        player (str): The name of the player who took the last stick.
    """
    print(f"\n{player} took the last stick. {player} wins!")


def play_game(
    players: list[str], starting_player_index: int, computer_choice_function=None
):
    """
    Main game loop to play the game of 21 sticks.

    Args:
        players (list[str]): List of player names.
        starting_player_index (int): Index of the starting player.
        computer_choice_function (function, optional): Function to determine the computer's move. Defaults to None.
    """
    sticks_pile = STICKS
    current_player_index = starting_player_index

    print(
        f"\n{sticks_pile} sticks in the pile. {players[current_player_index]} starts!"
    )
    while sticks_pile > 0:
        player = players[current_player_index]

        player_choice = handle_player_turn(
            player, sticks_pile, computer_choice_function
        )
        sticks_pile -= player_choice

        if sticks_pile <= 0:
            determine_winner(player)
            break

        print(f"\n{sticks_pile} sticks remaining in the pile.")
        current_player_index = get_next_player_index(players, current_player_index)
