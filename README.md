# Tic-Tac-Toe Meta-Game

A Python implementation of a variation of the classic game of tic-tac-toe, where players take turns putting X's and O's in a 3x3 grid. In this version, there are 9 instances of the game being played simultaneously, constituting a meta-game.

## Features

- **Meta-Game Structure:** The game instances are arranged in a 3x3 grid, constituting a meta-game.
- **Player Options:** Supports one or two players. In single-player mode, the computer acts as the second player.
- **Game Rules:** Players take turns making moves in any one of the 9 game instances. The first player to get 3 in a row in the meta-game wins.
- **Game Reset:** If a game instance results in a tie, it is replaced with a fresh instance with no moves played.
- **Interactive Interface:** Clear prompts and intuitive interface for player interaction.

## How to Play

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Run the `main.py` file to start the game.
4. Follow the on-screen instructions to select the number of players and make moves.

## Requirements

- Python 3.x

## Usage

```bash
python main.py
