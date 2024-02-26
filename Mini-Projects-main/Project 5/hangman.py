import random as rn
from words import words
import string
coount = 0
# to get words without space or hypen character
def get_valid_word(words):
    word = rn.choice(words)
    while '-' in word or ' ' in word :

        word = rn.choice(words)

    return word
    
def hangman():
    count = 0
    word = get_valid_word(words)
    word_letters = set(word.upper()) # letters in the word
    # print(word_letters)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = len(word_letters) + 5
    # getting user input
    while len(word_letters) > 0 and lives > 0 :
        # letter used
        
        # print(len(word_letters))
        print('You have ',lives,' lives left and you have used these letters: ', ' '.join(used_letters))

        # what they have gussed till now
        word_list = [letter.upper() if letter.upper() in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))

        user_letter = input("Guess a letter : ").upper()
        
        # print(f'user letter is,{user_letter}')
        if user_letter in alphabet - used_letters: # if user guessed letter is in the alphabet and not in the used_letter
            used_letters.add(user_letter) # add the guessed letter to the used_letter
            # print(used_letters)
            if user_letter in word_letters :
                word_letters.remove(user_letter) # removing the gussed letter if it is present in the letter of the word to be guessed
                # print(word_letters)
                count = count + 1
            else:
                lives = lives - 1
                print("Letter not in the word")
        elif user_letter in used_letters :
            print("You have already used that character. Please try again ")
            
        else:
            print("Enter a valid character. ")

    if lives == 0 :
        print(f'Sorry you lost, the word was {word.upper()}')
    else:    
        word_list = [letter.upper() if letter.upper() in used_letters else '-' for letter in word]
        print(f'You guessed the word correctly with {count} guesses : ',' '.join(word_list))



hangman()







