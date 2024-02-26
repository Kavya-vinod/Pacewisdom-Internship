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
