import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too Low.')
        elif guess > random_number:
            print('Sorry, guess again. Too High.')
    
    print(f'Yay, Congrats. You have Guessed the number {random_number}')

guess(10)