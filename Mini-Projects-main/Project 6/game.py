from player import HumanPlayer,RandomComputerPlayer
import time
class TicTacToe:
    # board 3 * 3
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)] # list to represent a single 3 * 3 board
        self.current_winner = None # keeps track of the winner
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # 0,1,2 - 1st row, 3,4,5 - 2nd row, 6,7,8 - 3rd row
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (shows which number corresponds to which box )
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |') # + ' | '.join(row) + --> 0 | 1 | 2

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']
        ''' moves = []
        for (i,spot) in enumerate(self.board): # list of the index and what is present in the index
            # ['x' ,'o' ,'o'] --> [(0, 'x'),(1, 'x'),(2, 'o')]

            if spot == ' ':
                moves.append(i) # index at which moves are available
        return moves '''
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make the move by assigning the letter to the square
        # then return true
        # if invalid return false
        if self.board[square] == ' ' :
            self.board[square] = letter
            if self.winner(square, letter): # to check for a winner after each move
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row or 3 in a column  or 3 in a diagonal anywhere
        # check row
        row_ind = square // 3  # i.e, 0,1,2//3 == 0th row
        row = self.board[ row_ind*3 : (row_ind + 1) * 3 ] # [0:3] if row_ind = 0
        if all([spot == letter for spot in row]): # if all letters in the row is the same as the letter then return true
            return True
        
        # check column
        col_ind = square % 3 # if 0th column --> 0 mod 3 == 0, 1 mod 3 == 1st column
        column = [self.board[col_ind+i*3] for i in range(3)] # id col_ind = 1 ,then column=[1,4,7] ,i.e [1+(0*3), 1+(1*3), 1+(2*3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check for diagonal[0,4,8,] or [2,4,6]
        if square % 2 == 0:
            diagonal1= [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            
            diagonal2= [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all ([spot == letter for spot in diagonal2]):
                return True
        # no winner  
        return False

def play(game, x_player, o_player, print_game=True):
# return the winner if there is one, else returns None ,i.e a tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # (we return the one that breaks the loop ,hence no worries about thw winner)
    while game.empty_squares():
        # get the move from the appropriate player.
        if letter == 'O':
            square = o_player.get_move(game)
            # print(square)
        else:
            square = x_player.get_move(game)
            # print(square)
    
        # function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # empty line

            if game.current_winner:
                if print_game:
                    print(letter + " wins the game ")
                return letter
            

            letter = 'O' if letter == 'X' else 'X'
            # if letter == 'X':
            #   letter = 'O'
            # else:
            #   letter = 'X
        # pause
        time.sleep(1) 
    if print_game:
        print("It's a tie ")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe() # t is the instance of TicTacToe
    play(t, x_player, o_player, print_game=True)

        

