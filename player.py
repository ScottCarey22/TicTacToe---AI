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

class UnbeatablePlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # randomly choose a valid move          
            square = random.choice(game.available_moves())
        else:
            # get the square based off the minimax alogirthm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # base case: first check if prev move is a winner
        if state.current_winner == other_player:
        # return position and score so we can keep track of score for algorithm to work
            return {'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1*(state.num_empty_squares() + 1)}
        # no empty squares
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
        # each score should maximize
            best = {'position': None,'score': -math.inf}
        else:
        # each score should minimize
            best = {'position': None,'score': math.inf}

        for possible_move in state.available_moves():
        # step 1: make a move, try that spot
            state.make_move(possible_move, player)
        # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)
        # step 3: undo the move
            state.board[possible_move] =' '
            state.current_winner = None
            sim_score['position'] = possible_move
        # step 4: update the dicitionaries if necessary
            if player == max_player:
            # maximize
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
            # minimize
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best





    


