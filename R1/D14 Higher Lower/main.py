#higher-lower game

import random
from replit import clear

#import art pieces
from art import logo
from art import vs

#import the game data dictionary
from game_data import data

##game function def begin
def game():
    # init score
    score = 0
    # init gameover flag
    gameover = False
    # init guess variables A and B

    choice_a = {}
    choice_b = {}
    choice_a['follower_count'] = 0
    choice_b['follower_count'] = 0

    #playloop here
    while gameover is False: 
        #clear screen
        clear()
        #print the logo
        print(logo)

        if score > 0:
            print (f"You're right! Current score: {score}.")
        ## load in data to A and B. 
        # if B is non-zero then A = B
        if choice_b['follower_count'] != 0:
            choice_a = choice_b
        else:
        # otherwise load a random entry into A and remove it from the dictionary
            index = random.randint(0, len(data) - 1)
            # print (index)
            choice_a = data[index]
            del data[index]

        # load a random entry into B and remove it from the dictionary
        index = random.randint(0, len(data) - 1)
        choice_b = data[index]
        del data[index]
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
        user_response = input("Who has more followers? Type 'A' or 'B': ")
        
        ## calculate the answer, probably move to a function to calc the answer
        answer = "0" # init answer
        a_count = int(choice_a['follower_count'])
        b_count = int(choice_b['follower_count'])
        if a_count > b_count:
            answer = "a"
        else:
            answer = "b"

        ## compare response to answer
        user_response = user_response.lower()
        # if the response is wrong, set gameoverflag
        if user_response != answer:
            print ("NOPE")
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
