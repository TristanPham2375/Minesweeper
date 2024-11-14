# Imports
from table import Table

print("MineSweeper!")
print()

table = Table()

table.display_board()

game = table.is_game_over()

while game == False:
    result = table.player_choose_cell()

    if result == "Game Over":
        break

    if table.check_win():
        print("Congratulations! You have revealed all non-mine cells and won the game!")
        break

    print("\nCurrent board:")
    table.display_board()
