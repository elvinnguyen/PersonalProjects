import math
import time
from Player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] # we will use a single list to represent 3x3 board
        self.current_winner = None # keep track of winner 

    def print_board(self): 
        # i * 3 to (i + 1) * 3 is saying which group of 3 spaces are we choosing (1st, 2nd, or 3rd) 
        # just getting the rows 
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]: 
            print("| " + " | ".join(row) + " |") 

    @staticmethod
    def print_board_nums(): 
        # 0 | 1 | 2. tells us which number corresponds to what box
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |") 

    def available_moves(self):
        # list comprehension 
        # condenses whole for loop into single line 
        return [i for i, spot in enumerate(self.board) if spot == " "]
        """
        moves = []
        for(i , spot) in enumerate(self.board):
            # ["x", "x", "o"] --> [(0, "x"), (1, "x"), (2, "o")]
            if spot == " ": 
                moves.append(i)
        return moves 
        """

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        # can return len(self.available_moves())
        return self.board.count(" ") 

    def make_move(self, square, letter): 
        # if valid move, then make the move (assign square to letter)
        # then return ture. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner is if ther is 3 in a row
        # first check 3 in a row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        # check column
        col_ind = square % 3 
        column = [self.board[col_ind + (i * 3)] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # check diagonal 
        # but only if squares are an even number (0, 2, 4, 6, 8)
        # these are the only moves to win a diagonla 
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal 
            if all([spot == letter for spot in diagonal1]):
                return True 
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # righ to left diagonal 
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all the checks fail 
        return False 

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X" # starting letter 
    # will continue iterating if game still has empty squares
    # (we don't have to worry about winner because we'll just return that which breaks for loop)
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" make a move to square {square}")
                game.print_board()
                print("")  # just an empty line 

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter 
            # after we make move, we need to alternate letters
            letter = "O" if letter == "X" else "X" # switches players 
            """
            same as
            if letter == "X":
                letter = "O"
            else: 
                letter = "X"
            """
        
        # tiny break
        if print_game:
            time.sleep(0.8)

    if print_game:
        print("It\'s a tie!")

if __name__ == "__main__":
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(10):
        x_player = RandomComputerPlayer("X") 
        o_player = GeniusComputerPlayer("O")
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False) 
        if result == "X":
            x_wins += 1
        elif result == "O":
            o_wins += 1
        else:
            ties += 1
    print(f"After 10 iterations, we see {x_wins} X wins, {o_wins} O wins, and {ties} ties") 