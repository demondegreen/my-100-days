#Number Guessing Game Objectives:

import random
chosen_number = random.randint(1,100)

# startup display
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Hint: the number is {chosen_number}.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
if difficulty == 'hard':
    turns_left = 5
else:
    turns_left = 10 # for invalid entries, just default to easy

def penalize_player(_turns_left):
    _turns_left -=1
    if _turns_left == 0:
        print("Out of turns, you lose!")
        return 0
    else:
        print("Guess again.")
        return _turns_left

#main game loop, this game does not have repeat option.
gameover = False # Flip to true if player guesses, else game ends at 0 turns.
while turns_left > 0 and gameover == False:
    print(f"You have {turns_left} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        print(f"That's it, the number is {chosen_number}!")
        gameover = True
    elif guess < chosen_number:
        print("Too low.")
        turns_left = penalize_player(turns_left)
    else:
        print("Too high.")
        turns_left = penalize_player(turns_left)
