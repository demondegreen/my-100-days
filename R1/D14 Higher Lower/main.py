# higher-lower game

import random
# from replit import clear

# import art pieces
from art import logo, vs

# import the game data dictionary
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


def format_entry_string(_entry):
    name = _entry['name']
    description = _entry['description']
    country = _entry['country']
    return f"{name}, {description}, from {country}."


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

    # playloop begin
    while gameover is False:
        # clear()
        print(logo)
        # load in data to A and B.
        if score > 0:
            print(f"You're right! Current score: {score}.")
            choice_a = choice_b
        else:
            # otherwise load a random entry into A and remove it from the dictionary
            choice_a = get_entry()
        # load a random entry into B and remove it from the dictionary
        choice_b = get_entry()

        # print the A data string
        print("Compare A: " + format_entry_string(choice_a))

        # print the "VS" art
        print(vs)

        # print the B data string
        print(f"Against B: " + format_entry_string(choice_b))

        # print the input prompt
        user_response = input("Who has more followers? Type 'A' or 'B': ").lower()

        # calculate the answer, moved to a function to calc the answer
        answer = get_answer(choice_a, choice_b)

        # compare response to answer
        # if the response is wrong, set gameoverflag
        if user_response != answer:
            gameover = True
            # print the losing message
            print(f"Sorry, that's wrong. Final score: {score}")
        # else increment score and continue
        else:
            score += 1
            if len(data) == 0:  # deck is empty, game ends
                gameover = True
            # print the rare winning message
            print(f"Wow, you cleared the deck.  You win. Final score: {score}")
    # playloop end


# game function def end

game()
