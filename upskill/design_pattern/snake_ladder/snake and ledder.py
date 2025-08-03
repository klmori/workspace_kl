import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1

class Board:
    def __init__(self, size, snakes, ladders):
        self.size = size
        self.snakes = snakes
        self.ladders = ladders

    def move(self, position):
        if position in self.snakes:
            print(f"Oops! Snake from {position} to {self.snakes[position]}")
            return self.snakes[position]
        if position in self.ladders:
            print(f"Yay! Ladder from {position} to {self.ladders[position]}")
            return self.ladders[position]
        return position

class Dice:
    def roll(self):
        return random.randint(1, 6)

class Game:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.dice = Dice()

    def play(self):
        while True:
            for player in self.players:
                input(f"{player.name}'s turn. Press enter to roll dice...")
                roll = self.dice.roll()
                print(f"{player.name} rolled a {roll}")
                new_pos = player.position + roll
                if new_pos > self.board.size:
                    print("Roll too big, skipping...")
                    continue
                player.position = self.board.move(new_pos)
                print(f"{player.name} moved to {player.position}")
                if player.position == self.board.size:
                    print(f"{player.name} wins!")
                    return

# --- Setup & Run ---
snakes = {17: 7, 54: 34, 62: 19, 98: 79}
ladders = {3: 38, 24: 33, 42: 93, 72: 84}
board = Board(100, snakes, ladders)
players = [Player("Alice"), Player("Bob")]
game = Game(players, board)
# game.play()
