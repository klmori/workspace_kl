import random
from collections import deque

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0


class Board:
    def __init__(self, size=100):
        self.size = size
        self.snakes = {}  # key: head, value: tail
        self.ladders = {}  # key: bottom, value: top

    def set_snakes(self, snakes):
        self.snakes = snakes

    def set_ladders(self, ladders):
        self.ladders = ladders

    def check_snake_or_ladder(self, position):
        if position in self.snakes:
            return self.snakes[position]
        elif position in self.ladders:
            return self.ladders[position]
        return position



class Dice:
    def roll(self):
        return random.randint(1, 6)




class Game:
    def __init__(self, players, board, dice):
        self.players = deque(players)
        self.board = board
        self.dice = dice

    def start(self):
        while True:
            current_player = self.players.popleft()
            roll = self.dice.roll()
            print(f"{current_player.name} rolls a {roll}")
            new_pos = current_player.position + roll

            if new_pos > self.board.size:
                print(f"{current_player.name} can't move")
            else:
                new_pos = self.board.check_snake_or_ladder(new_pos)
                print(f"{current_player.name} moves to {new_pos}")
                current_player.position = new_pos

                if new_pos == self.board.size:
                    print(f"{current_player.name} wins!")
                    break

            self.players.append(current_player)


if __name__ == "__main__":
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    board = Board()
    board.set_snakes(snakes)
    board.set_ladders(ladders)

    players = [Player("Alice"), Player("Bob")]
    dice = Dice()
    # test = deque(players)
    # p = test.popleft()
    # print(p.name)
    # p = test.popleft()
    # print(p.name)
    game = Game(players, board, dice)
    # game.start()



# playe  urrent_turn)
    
