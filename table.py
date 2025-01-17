import random


class Node:
    def __init__(self):
        """
        Initializes a box in the game.

        use: Creates a new node with initial values for value, revealed state, and all 8 neighbors.
        parameters: None
        return: None
        """
        self.value = None
        self.revealed = False

        # Initialize neighbor pointers
        self.up = None
        self.rightup = None
        self.right = None
        self.rightdown = None
        self.down = None
        self.leftdown = None
        self.left = None
        self.leftup = None


class Table:
    def __init__(self):
        """
        Initializes a 9x9 mine sweeper table consisting of nodes.

        use: Initializes a 9x9 grid of nodes, connects neighbors, places mines, and counts surrounding mines.
        parameters: None
        return: None
        """
        self.grid = [[Node() for _ in range(9)] for _ in range(9)]

        self._connect_neighbors()
        self.place_mines()
        self.mine_count()
        self.game_over = False

        self.width = 9
        self.height = 9

        # Diagnostic: Check grid dimensions
        print("Grid dimensions:", len(self.grid), "x", len(self.grid[0]))

    def _connect_neighbors(self):
        """
        Connect each node to its surrounding neighbors.

        use: Links each node to its adjacent nodes (up, down, left, right, diagonals).
        parameters: None
        return: None
        """
        for i in range(9):
            for j in range(9):
                current_node = self.grid[i][j]

                current_node.up = current_node.rightup = current_node.right = None
                current_node.rightdown = current_node.down = current_node.leftdown = None
                current_node.left = current_node.leftup = None

                if i > 0:
                    current_node.up = self.grid[i - 1][j]
                if i < 8:
                    current_node.down = self.grid[i + 1][j]
                if j > 0:
                    current_node.left = self.grid[i][j - 1]
                if j < 8:
                    current_node.right = self.grid[i][j + 1]
                if i > 0 and j > 0:
                    current_node.leftup = self.grid[i - 1][j - 1]
                if i > 0 and j < 8:
                    current_node.rightup = self.grid[i - 1][j + 1]
                if i < 8 and j > 0:
                    current_node.leftdown = self.grid[i + 1][j - 1]
                if i < 8 and j < 8:
                    current_node.rightdown = self.grid[i + 1][j + 1]

    def place_mines(self):
        """
        Randomly assigns mines to 10 nodes in the 9x9 grid.

        use: Randomly places 10 mines on the grid by assigning a value of 99 to selected nodes.
        parameters: None
        return: None
        """
        positions = [(i, j) for i in range(9) for j in range(9)]
        mine_positions = random.sample(positions, 10)

        for (i, j) in mine_positions:
            self.grid[i][j].value = 99

    def mine_count(self):
        """
        Assigns an integer value to each node indicating the count of surrounding mines.

        use: Calculates the number of mines adjacent to each non-mined node.
        parameters: None
        return: None
        """
        for i in range(9):
            for j in range(9):
                current_node = self.grid[i][j]

                if current_node.value == 99:
                    continue

                neighbors = [
                    current_node.up, current_node.rightup, current_node.right,
                    current_node.rightdown, current_node.down, current_node.leftdown,
                    current_node.left, current_node.leftup
                ]

                mine_count = 0
                for neighbor in neighbors:
                    if neighbor and neighbor.value == 99:
                        mine_count += 1

                current_node.value = mine_count

    def reveal_cell(self, row, col):
        """
        Reveals the value of a cell, and if the value is 0, reveals surrounding cells.

        use: Reveals a specific cell and triggers the reveal of surrounding cells if the value is 0.
        parameters: 
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        return: None
        """
        node = self.grid[row][col]

        if node.value == 99:
            self.reveal_board()
            self.game_over = True
            return

        self._reveal_recursive(row, col)

    def _reveal_recursive(self, row, col):
        """
        Helper function to recursively reveal cells with 0 value.

        use: Recursively reveals adjacent cells with a value of 0 and their neighbors.
        parameters:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        return: None
        """
        if not (0 <= row < 9 and 0 <= col < 9):
            return

        node = self.grid[row][col]

        if node.revealed or node.value == 99:
            return

        node.revealed = True
        if node.value == 0:
            neighbors = [
                (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
                (row - 1, col - 1), (row - 1, col +
                                     1), (row + 1, col - 1), (row + 1, col + 1)
            ]
            for r, c in neighbors:
                self._reveal_recursive(r, c)

    def check_win(self):
        """
        Checks if all non-mined cells are revealed.

        use: Checks if all non-mined cells have been revealed, indicating the player has won.
        parameters: None
        return: bool: True if the player has won, False otherwise.
        """
        if self.game_over:
            return False

        for row in self.grid:
            for node in row:
                if node.value != 99 and not node.revealed:
                    return False
        return True

    def reveal_board(self):
        """
        Reveals the entire board.

        use: Reveals all cells on the board.
        parameters: None
        return: None
        """
        for row in self.grid:
            for node in row:
                node.revealed = True

    def display_board(self):
        """
        Displays the board as a 9x9 grid.

        use: Prints the board with revealed values and 'X' for unrevealed cells.
        parameters: None
        return: None
        """
        for row in self.grid:
            line = []
            for node in row:
                if not node.revealed:
                    line.append("X")
                elif node.value == 99:
                    line.append("M")
                else:
                    line.append(str(node.value))
            print(" ".join(line))

    def player_choose_cell(self):
        """
        Prompts the player to select a cell to reveal by entering row and column coordinates.

        use: Allows the player to input the row and column of the cell they want to reveal.
        parameters: None
        return: None
        """
        if self.game_over:
            return "Game Over"

        row_input = input(
            "Enter the row (1-9) of the cell you want to reveal: ")
        col_input = input(
            "Enter the column (1-9) of the cell you want to reveal: ")

        if row_input.isdigit() and col_input.isdigit():
            row = int(row_input) - 1
            col = int(col_input) - 1

            if 0 <= row < 9 and 0 <= col < 9:
                self.reveal_cell(row, col)
            else:
                print("Please enter row and column values between 1 and 9.")
        else:
            print("Please enter valid integer values for row and column.")

    def is_game_over(self):
        """
        Returns game_over status.

        use: Returns the status of the game, indicating if it is over.
        parameters: None
        return: bool: True if the game is over, False otherwise.
        """
        return self.game_over
