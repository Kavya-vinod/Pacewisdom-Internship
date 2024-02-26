import random as rn

def guess(x):
    random_number = rn.randint(1, x)
    guess = 0
    while guess != random_number :
        guess = int(input(f"Guess a number between 1 and {x} : "))
        if guess < random_number :
            print("Sorry, you got another chance to guess. Too low.")
        elif guess > random_number :
            print("Sorry, you got another chance to guess. Too high.")
    
    print(f"Hurray, You guess is perfect. ")

guess(35)
