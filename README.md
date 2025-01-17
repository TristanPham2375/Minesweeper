# Minesweeper 

A fully playable Minesweeper game developed in Python. This game replicates the classic Minesweeper experience with randomly placed mines, grid generation, value assignment, and recursive node reveal.

## 🎮 Features

- **Randomized Mine Placement**: Each game begins with mines randomly distributed across the grid.
- **Grid Generation**: Dynamic grid creation with a fixed 9x9 size, but adaptable to changes in the code.
- **Node Reveal Using Recursion**: Reveals nodes recursively, uncovering safe cells automatically if the value is 0.
- **Game Logic**: Automatically calculates neighboring mine counts for each cell and manages game win/lose states.
- **User Input**: Prompts the player to select a cell and reveal it. The game will handle invalid inputs.

## 💻 Technologies Used

- **Language**: Python
- **Design Principles**: Object-Oriented Programming (OOP) for modularity and clarity.
- **Core Algorithms**: 
  - Recursion for node reveal.
  - Randomization for mine placement.

## 📂 Project Structure

- `main.py`: The main program file, initializes the game, handles user input, and manages game logic.
- `table.py`: Defines the table layout, including cell properties and methods for mine placement, value assignment, and recursive reveal.
- `Node`: A class that defines the properties of each cell in the grid, including neighbors, revealed status, and mine value.
- `Table`: A class that defines the 9x9 grid, including methods to set up the grid, place mines, calculate neighboring mines, and reveal cells.

## 🚀 How to Play

1. **Start the Game**: Run `main.py` to start the game.
2. **Choose a Cell**: Enter the row and column (1-9) of the cell you want to reveal. Avoid hitting mines!
3. **Winning the Game**: The game ends when all non-mine cells are revealed. If you reveal a mine, the game is over.
4. **Game Over**: The game ends if you hit a mine, and all cells will be revealed.

## 📋 Instructions

- The grid is a 9x9 matrix.
- The objective is to reveal all the non-mine cells.
- You can choose any cell to reveal by entering the row and column numbers (1-9).
- If a cell contains a number, it indicates how many mines are adjacent to it.
- If a cell contains a mine, the game ends.

