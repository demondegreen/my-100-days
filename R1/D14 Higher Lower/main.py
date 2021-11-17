#higher-lower game

import random
from replit import clear

#import art pieces
from art import logo
from art import vs

#import the game data dictionary
from game_data import data

def get_answer(_a, _b):
    """
    Returns the greater between inputs as string "a" or "b"
    """
    a_count = int(_a['follower_count'])
    b_count = int(_b['follower_count'])
    if a_count > b_count:
        return "a"
    else:
        return "b"

def get_entry():
    """
    pulls an entry permanently off the global data stack and returns that entry
    """
    index = random.randint(0, len(data) - 1)
    entry = data[index]
    del data[index]
    return entry

##game function def begin
def game():
    # init score
    score = 0
    # init gameover flag
    gameover = False
    # create and init entry variables A and B

    choice_a = {}
    choice_b = {}
    choice_a['follower_count'] = 0
    choice_b['follower_count'] = 0

    #playloop begin
    while gameover is False: 
        clear()
        print(logo)
        if score > 0:
            print (f"You're right! Current score: {score}.")
            
        ## load in data to A and B. 
        # if B is non-zero then A = B, could also test if score > 0
        if choice_b['follower_count'] != 0:
            choice_a = choice_b
        else:
        # otherwise load a random entry into A and remove it from the dictionary
            choice_a = get_entry()
        # load a random entry into B and remove it from the dictionary
        choice_b = get_entry()

        #print the A data string
        a_name = choice_a['name']
        a_description = choice_a['description']
        a_country = choice_a['country']
        print(f"Compare A: {a_name}, {a_description}, from {a_country}.")

        #print the "VS" art
        print(vs)

        #print the B data string
        b_name = choice_b['name']
        b_description = choice_b['description']
        b_country = choice_b['country']
        print(f"Against B: {b_name}, {b_description}, from {b_country}.")

        # print the input prompt
        user_response = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        ## calculate the answer, moved to a function to calc the answer
        answer = get_answer(choice_a, choice_b)

        ## compare response to answer
        # if the response is wrong, set gameoverflag
        if user_response != answer:
            gameover = True
        # else increment score and continue
        else:
            score += 1
    # playloop end

    # print the final message, everybody loses eventually there is no win condition.
    print(f"Sorry, that's wrong. Final score: {score}")

## game function def end

#call game()
game()
