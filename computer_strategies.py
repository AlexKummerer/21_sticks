import random
from constants import DIFFICULTY_CONFIG


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
        return random.randint(1, min(3, sticks_pile))


def get_computer_choice_function(difficulty: str) -> callable:
    """
    Returns a function to determine the computer's move based on the selected difficulty.

    Args:
        difficulty (str): The selected difficulty level.

    Returns:
        callable: The function to use for the computer's move based on the difficulty.
    """
    optimal_move_probability = DIFFICULTY_CONFIG.get(difficulty, {}).get(
        "probability", 0.0
    )
    return lambda sticks_pile: computer_choice(sticks_pile, optimal_move_probability)
