# 21 Sticks Game

Welcome to the **21 Sticks Game**! This is a Python-based game where players take turns removing 1 to 3 sticks from a pile. The player who takes the last stick wins. You can play with multiple players, including a computer opponent with configurable difficulty levels.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Play](#how-to-play)
  - [Game Modes](#game-modes)
  - [Gameplay](#gameplay)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Multiple Players**: Play with 2 or more players.
- **Computer Opponent**: Play against a computer with adjustable difficulty levels.
- **Customizable Pile Size**: Set the initial number of sticks in the pile.
- **Simple and Fun**: Easy-to-understand rules and engaging gameplay.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system. Download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alexkummerer/21-sticks-game.git

2. **Navigate to the project directory**:
    cd 21-sticks-game
3. **Install dependencies**:
    The game doesn't require external dependencies other than Python itself, so no additional packages are needed.

### How to Play
## Game Modes
- **Two Players**: Play against another human player.
- **Player vs Computer**: Play against the computer with a choice of difficulty levels.

## Gameplay

1. ***Starting the Game***:

    Run the game using Python:
    python 21_sticks.py

2. ***Setup***:

- You will be prompted to enter the number of players and their names.
- Optionally, you can include a computer player.
- Set the initial number of sticks in the pile (default is 21 sticks).
3. ***Playing the Game***:
- Players take turns to remove 1 to 3 sticks from the pile.
- The game continues until the pile is empty.
- The player who takes the last stick wins.

4. ***Computer Difficulty***:

When playing against the computer, you can choose the difficulty level from:

- Low
- Medium-Low
- Medium
- Medium-High
- High

### Configuration
You can customize the game by modifying the constants defined in the constants.py file:

- **STICKS_DEFAULT**: The default number of sticks in the pile.
- **GAME_TITLE**: The title of the game.
- **COMPUTER_NAME**: The name used for the computer player.
- **PLAY_AGAIN_PROMPT**: The message prompt for replaying the game.
- **GOODBYE_MESSAGE**: The message displayed when exiting the game.
- **DIFFICULTY_CONFIG**: A dictionary defining the probabilities and descriptions for the computer difficulty levels.



License
This project is licensed under the MIT License. See the LICENSE file for more details.