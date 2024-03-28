import math
import random


class Player:
    def __init__(self, letter):
        # player is letter x or o
        self.letter = letter


    # want all players to get their next move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square



class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        while not valid_square:
            square = input(self.letter + '\'s turn. Choose a square from (0 - 8): ')

            try:
                square = int(square)
                if square not in game.available_moves():
                    raise ValueError
                valid_square = True
                break
            except ValueError:
                print('Invalid square, Try again')
        return square
