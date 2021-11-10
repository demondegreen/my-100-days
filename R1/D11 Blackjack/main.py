## Blackjack
import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """
    Returns one blackjack card number value.  Ace returned as 11. Infinite deck.
    """
    return random.choice(cards)

def player_hand_total(hand):
    """
    Returns the total of a given hand taking into account the rules for the ace on the PLAYER'S turn. DO NOT USE FOR DEALER RESOLUTION.
    """
    total = 0
    for card in hand:
        if card == 11 and total + card > 21:
            total +=1
        else:
            total += card
    return total

def main_loop():
    global play_again
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        print(logo)

        #init hands
        player_hand = []
        dealer_hand = []

        player_total = 0
        dealer_total = 0

        # first deal is 2 for each ... these setup loop state
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

        player_total = player_hand_total(player_hand)
        dealer_total = sum(dealer_hand)

        if player_total == 21 and dealer_total == 21:
            print(f"Your cards: {player_hand}, current score: {player_total}")
            print(f"Computer's first cards: {dealer_hand}")
            print ("PUSH 21 LAME  YOU LOSE")
        elif player_total == 21:
            print(f"Your cards: {player_hand}, current score: {player_total}")
            print(f"Computer's first card: {dealer_hand[0]}")
            print ("Natural 21 YOU WIN")
        elif dealer_total == 21:
            print(f"Your cards: {player_hand}, current score: {player_total}")
            print(f"Computer's first card: {dealer_hand}")
            print ("Dealer got a natural 21 YOU LOSE")
        else:
            print(f"Your cards: {player_hand}, current score: {player_total}")
            print(f"Computer's first card: {dealer_hand[0]}")

            player_turn = True
            game_resolved = False
            while player_turn:
                if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                    hit_player = True
                else:
                    hit_player = False
                    player_turn = False # move on to dealer resolution

                while hit_player: 
                    player_hand.append(deal_card())
                    player_total = player_hand_total(player_hand)
                    print(f"Your cards: {player_hand}, current score: {player_total}")
                    print(f"Computer's first card: {dealer_hand[0]}")
                    # resolve hit results
                    if player_total > 21:
                        print ("BUSTED YOU LOSE!")
                        player_turn = False
                        game_resolved = True
                    elif player_total == 21:
                        print("21 YOU WIN!")
                        player_turn = False
                        game_resolved = True
                    hit_player = False
            
            if not game_resolved: # Resolve game, dealer deals to 17 only run if the player is not busted
                while dealer_total < 17:
                    dealer_hand.append(deal_card())
                    dealer_total = sum(dealer_hand) # simpler ace rules for Dealer
                print(f"Your cards: {player_hand}, current score: {player_total}")
                print(f"Computer's hand: {dealer_hand} dealer score {dealer_total}")
                if dealer_total <= 21 and dealer_total > player_total:
                    print("Dealer wins!")
                elif dealer_total < 21 and dealer_total == player_total:
                    print("Push! LAME")
                elif dealer_total >= 17 and dealer_total < player_total:
                    print("Dealer stands on 17.  You win!")
                elif dealer_total > 21:
                    print("Dealer busts! You win!")
    else:
        play_again = False

#run game
play_again = True #run game at least once
while play_again:
    main_loop()
