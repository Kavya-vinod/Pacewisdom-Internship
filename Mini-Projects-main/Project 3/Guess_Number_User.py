import random as rn 

def computer_guess(x) :
    low = 1
    high = x
    feedback = ""
    while feedback != "c" and low != high :
        
        guess = rn.randint(low, high)
    
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C): ")
        if feedback == 'h' :
            guess=guess-1
            high = guess
        if feedback == 'l' :
            guess=guess+1
            low = guess
    
    print(f"Hurray! The computer guessed your number, {guess}, correctly!")

computer_guess(10)

