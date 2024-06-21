STICKS = 21


GAME_TITLE = "Welcome to the Game 21 Sticks"
PLAYER_1 = "Player 1"
PLAYER_2 = "Player 2"
PLAY_AGAIN_PROMPT = "Do you want to play again? (yes/no): "


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

def choose_sticks(prompt: str, max_sticks:int) -> int:
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


def two_player_game():
    """
    Play a two-player game of 21 sticks.
    """
    players = [PLAYER_1, PLAYER_2]
    current_player_index = 0
    sticks_pile = STICKS
    
    print(f"{sticks_pile} sticks in the pile.")
    while sticks_pile > 0:
        player = players[current_player_index]
        print(f"\n{player}'s turn.")
        
        max_sticks = min(3, sticks_pile)
        player_choice = choose_sticks(prompt=f"{player}, how many sticks do you take (1-{max_sticks})? ", max_sticks=max_sticks)
        sticks_pile -= player_choice
                
        if sticks_pile <= 0:
            print(f"\n{player} took the last stick. {players[get_next_player_index(players, current_player_index)]} wins!")
            break
        
        print(f"\n{sticks_pile} sticks remaining in the pile.")

        current_player_index = get_next_player_index(players, current_player_index)

def main(): 
    
    print(GAME_TITLE)
    while True:
        two_player_game()
        if not play_again():
            break

if __name__ == "__main__":
    main()
