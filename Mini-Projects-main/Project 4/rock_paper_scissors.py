import random as rn

def play():
    user = input("What is your choice ? 'r' for rock, 'p' for paper, 's' for scissors .\n" )
    computer = rn.choice(['r', 'p' ,'s'])

    # rules
    if user == computer :
        return 'It\'s a tie'
    
    if is_winner(user, computer):
        return 'You won'
    
    return 'You lost!'
# rules : r > s, s > p, p > r 
def is_winner(player, opponent):
    # return 
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())