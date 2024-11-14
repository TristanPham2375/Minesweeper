# Minesweeper
A fully playable Minesweeper game developed in Python. This game replicates the classic Minesweeper experience with randomly placed mines, grid generation, value assignment, and recursive node reveal.

🎮 Features
Randomized Mine Placement: Each game begins with mines randomly distributed across the grid.
Grid Generation: Dynamic grid creation with custom size options.
Node Reveal Using Recursion: Reveals nodes recursively, uncovering safe cells automatically.
Game Logic: Automatically calculates neighboring mine counts for each cell and manages game win/lose states.

💻 Technologies Used
Language: Python
Design Principles: Object-Oriented Programming (OOP) for modularity and clarity
Core Algorithms: Recursion for node reveal, randomization for mine placement

📂 Project Structure
main.py: The main program file, initializes the game, handles user input, and manages game logic.
table.py: Defines the table layout, including cell properties and methods for mine placement, value assignment, and recursive reveal.
