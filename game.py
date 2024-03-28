from player import Player, RandomComputerPlayer, HumanPlayer, UnbeatablePlayer
import time

class TicTacToe:
    def __init__(self):
        # use a single list to rep a 3x3 board
        self.board = [' ' for _ in range(9)]
        # keep track of winner
        self.current_winner = None 
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'+'| '.join(row) +'|')

    @staticmethod
    def print_board_nums():
        #  0 | 1 | 2 tells use what number corresponds to the space
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+'| '.join(row) +'| ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return len(self.available_moves())
    

    # if valid move, make the move for the correct player
    # return true. if invalid, return False
    def make_move(self, square, letter):
        if square not in self.available_moves():
            return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner is 3 in a row any where (row, column, diagonal)
        # check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # check column 
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    
def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game letter or none
    if print_game:
        game.print_board_nums()

    # starting letter is X
    # iterate while gmae still has empty squares
    letter = 'X' 
    while game.empty_squares():
        # appropriate players move
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' made a move in square {square}')
                game.print_board()
                print('')
            else:
                print("Invalid move, try again")

            # check if game is over after move
            if game.current_winner:
                if print_game:
                    print(letter + ' has won!')
                return letter
 
        # switch players
            # if x then o, if o then x 
        letter = 'O' if letter == 'X' else 'X'

        # time between turns
        time.sleep(0.8)

    if print_game:
        print('It/s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = UnbeatablePlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

            
    
    