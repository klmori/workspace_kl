class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current = "X"

    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def move(self, row, col):
        if self.board[row][col] != " ":
            print("Cell already taken!")
            return False
        self.board[row][col] = self.current
        return True

    def check_winner(self):
        b = self.board
        # Rows, Columns
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != " ":
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != " ":
                return b[0][i]
        # Diagonals
        if b[0][0] == b[1][1] == b[2][2] != " ":
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != " ":
            return b[0][2]
        return None

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def switch_player(self):
        self.current = "O" if self.current == "X" else "X"

    def play(self):
        while True:
            self.display()
            print(f"Player {self.current}'s turn.")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid move!")
                continue
            if not self.move(row, col):
                continue
            winner = self.check_winner()
            if winner:
                self.display()
                print(f"Player {winner} wins!")
                break
            if self.is_draw():
                self.display()
                print("It's a draw!")
                break
            self.switch_player()

# --- Run it ---
# t = TicTacToe()
# t.play()
