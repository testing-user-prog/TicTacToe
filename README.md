# Tic-Tac-Toe with Minimax AI

A classic 3x3 Tic-Tac-Toe game built in Python, featuring an unbeatable AI opponent powered by the Minimax algorithm. The game has a graphical interface built with Pygame, letting you play as X or O against the computer.

## Features

- Playable GUI built with Pygame
- Choose to play as X or O
- AI opponent that uses the Minimax algorithm to always play optimally (win or draw, never lose)
- "Play Again" option to restart the game after it ends

## How It Works

The project is split into two files:

- **`tictactoe.py`** — Contains all the core game logic:
  - `initial_state()` — sets up an empty board
  - `player(board)` — determines whose turn it is
  - `actions(board)` — returns all valid moves
  - `result(board, action)` — returns the resulting board after a move
  - `winner(board)` — checks rows, columns, and diagonals for a winner
  - `terminal(board)` — checks if the game has ended
  - `utility(board)` — scores a finished game (1 for X win, -1 for O win, 0 for tie)
  - `minimax(board)` — recursively explores possible moves to find the optimal one

- **`runner.py`** — Handles the graphical interface using Pygame:
  - Lets the user pick a side (X or O)
  - Renders the board and handles click events for user moves
  - Calls into `tictactoe.py` for the AI's moves
  - Displays game status (whose turn it is, thinking state, win/tie) and a restart button

## Requirements

- Python 3
- [Pygame](https://www.pygame.org/)

Install Pygame with:

```bash
pip install pygame
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/testing-user-prog/TicTacToe.git
   cd TicTacToe
   ```
2. Make sure you have an `OpenSans-Regular.ttf` font file in the project directory (used for rendering text in the game window). Add it if it's missing.
3. Run the game:
   ```bash
   python runner.py
   ```

## How to Play

1. Launch the game — you'll be prompted to choose to play as X or O.
2. Click on an empty tile to make your move.
3. The AI will respond automatically using the Minimax algorithm.
4. The game announces a winner or a tie when it ends.
5. Click "Play Again" to start a new round.

## License

This project is open source and available for anyone to use or modify.
