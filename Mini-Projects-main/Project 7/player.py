# Minimax is decision making algorithm built of a maximizer and minimizer concept.
# Maximize your win while the opponent is trying to minimize their loss
# trys to find the best move by trying all the moves,and determining the optimal funtion using utility function 
# it is a measurement of how valuable the final result is in the decision tree.
# ex, Utility: 1 * 3 = 3
# based on the number of squares left, if it is tie then multiply with 0, if it is O's turn then multiply with -1,if x's turn then multiply with 1
# mulitpy with the number of squares left + 1
# ex, 1 * 2+1 = 3
# we use the max result when it is X's turn and use min result when it is O's turn

import math
import random

# base player class
class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
    
    # we want all players to get their next move in the game
    def get_move(self, game):
        pass # base player

# inheritance to ceate two players on top of the base class
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)   # call this initalising in the super class

    def get_move(self, game):
        square = random.choice(game.available_moves()) # a random spot
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square :
            square = input(self.letter + '\'s turn. Input move (0-8): ') # X's turn or O's turn
            # we have to check if the the user input is valid or not
            # we do this by casting it to an integer, and if it's not the we say as invalid
            # if that spot is not available on the board, we say it is invalid
            try : 
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            
            except ValueError:
                print('Invalid square. Try again')
        
        return val

class GeniusComputerPlayer(Player) :
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.avaialble_moves())
        else:
            # get the positon basd on the minimax algorithm that was described
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player): # only that particular state
        max_player = self.letter # you
        other_player = 'O' if player =='X' else 'X' # the other player

        # base cases
        # 1, check if the previous move is a winner
        if state.current_winner == other_player:
            # we should return positon and the score ,as we need to keep track of the score
            # for minimax to work
            return {'posiiton': None,
                    'score': 1 * (state.num_empty_squares() + 1 ) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
                    }
        elif not state.empty_squares():
            return {'positon':None,
                    'score' : 0
                    }
        if player == max_player:
            best = {'position': None,
                    'score': -math.inf} # each score should maximize
        else:
            best = {'positon': None,
                    'score': math.inf} # each score should minimize
            
        for possible_move in state.available_moves():
            # step 1 : make a move, try that spot
            state.make_move(possible_move, player)

            # step 2 : recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)  # to alternate players

            # step 3 : undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move # the simulated score of the positon that we just passed in


            # setp 4 : update dictionaries if necessary,i.e, if the score from this moves beats the current best score
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score


        return best

    
