class Game:
    """Object-oriented approach to Connect Four game."""

    def __init__(self, height, width, spacing):
        """Initialize the game board."""
        if ((height < 4) or (width < 4)):
            raise Exception("Board dimensions are too small.")

        if ((height > 25) or (width > 25)):
            raise Exception("Board dimensions are too large.")

        if (spacing < 0):
            raise Exception("Spacing cannot be less than 0.")

        self.height = height
        self.width = width
        self.spacing = " " * spacing
        self.matrix = [[" "
                        for i 
                        in range(self.width)] 
                        for j 
                        in range(self.height)]

    def print_board(self):
        """Display current state of game board."""
        for i in range(self.height):
            print(self.spacing + "|", end="")

            for j in range(self.width):
                print(self.matrix[i][j] + "|", end="")

            print()

    def add_move(self, column, piece):
        """Add piece to lowest available row for a column."""
        for i in reversed(range(self.height)):
            if (self.matrix[i][column] == " "):
                self.matrix[i][column] = piece
                break

    def valid_move(self, column):
        """Check if a column is out of range or full."""
        if ((column >= 0) and (column < self.width)):
            for i in range(self.height):
                if (self.matrix[i][column] == " "):
                    return True
        return False

    def is_full(self):
        """Check if the entire board is full."""
        for i in range(self.height):
            for j in range(self.width):
                if (self.matrix[i][j] == " "):
                    return False
        return True

    def check_win(self, piece):
        """Check if a 4-in-a-row combination exists on the board."""
        # Check horizontal.
        for i in range(self.height):
            for j in range(self.width - 3):
                if (self.matrix[i][j] == piece and
                    self.matrix[i][j + 1] == piece and
                    self.matrix[i][j + 2] == piece and
                    self.matrix[i][j + 3] == piece):
                        return True

        # Check vertical.
        for i in range(self.height - 3):
            for j in range(self.width):
                if (self.matrix[i][j] == piece and
                    self.matrix[i + 1][j] == piece and
                    self.matrix[i + 2][j] == piece and
                    self.matrix[i + 3][j] == piece):
                        return True

        # Check diagonal from upper left to bottom right.
        for i in range(self.height - 3):
            for j in range(self.width - 3):
                if (self.matrix[i][j] == piece and
                    self.matrix[i + 1][j + 1] == piece and
                    self.matrix[i + 2][j + 2] == piece and
                    self.matrix[i + 3][j + 3] == piece):
                        return True

        # Check diagonal from upper right to bottom left.
        for i in range(self.height - 3):
            for j in range(3, self.width):
                if (self.matrix[i][j] == piece and
                    self.matrix[i + 1][j - 1] == piece and
                    self.matrix[i + 2][j - 2] == piece and
                    self.matrix[i + 3][j - 3] == piece):
                        return True

        return False

    def check_tie(self):
        """Check if the game has ended in a draw."""
        return ((not self.check_win("X")) and 
                (not self.check_win("O")) and 
                self.is_full())

    def host_game(self):
        """Alternate players, populate board, and check for win/draw."""
        self.player = 1

        while True:
            if (self.player == 1):
                print(self.spacing + "Player 1's turn")
                self.player = 2
                move = int(input(self.spacing + "Enter a move (column): "))

                # Attempt to update board with player's move.
                if (self.valid_move(move)):
                    self.add_move(move, "X")
                else:
                    print(self.spacing + "Invalid move! Please try again.")
                    self.player = 1

                print()
                self.print_board()

                # Check if game has ended.
                if (self.check_win("X")):
                    print(self.spacing + "Player 1 has won the game!")
                    break

                if (self.check_tie()):
                    print(self.spacing + "The game has ended in a tie!")
                    break

            else:
                print(self.spacing + "Player 2's turn")
                self.player = 1
                move = int(input(self.spacing + "Enter a move (column): "))

                # Attempt to update board with player's move.
                if (self.valid_move(move)):
                    self.add_move(move, "O")
                else:
                    print(self.spacing + "Invalid move! Please try again.")
                    self.player = 2

                print()
                self.print_board()

                # Check if game has ended.
                if (self.check_win("O")):
                    print(self.spacing + "Player 2 has won the game!")
                    break

                if (self.check_tie()):
                    print(self.spacing + "The game has ended in a tie!")
                    break

# Start the game.
g = Game(6, 7, 4)
print()
print("Welcome to Connect Four!")
print()
g.print_board()
g.host_game()