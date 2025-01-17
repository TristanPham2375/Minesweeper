# Imports
from table import Table

print("MineSweeper!")
print()  #

table = Table()  # Initialize a new game table (9x9 grid)

table.display_board()  # Display the initial board to the player

game = table.is_game_over()  # Check if the game is over at the start

while game == False:
    # Prompt the player to choose a cell to reveal
    result = table.player_choose_cell()

    if result == "Game Over":  # If the player hits a mine, the game ends
        break

    if table.check_win():  # Check if the player has won by revealing all non-mine cells
        print("Congratulations! You have revealed all non-mine cells and won the game!")
        break

    print("\nCurrent board:")
    table.display_board()  # Display the board again after the player's move
