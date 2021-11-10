from replit import clear

bids = {} #init bid dict

clear()
from art import logo
print(logo)
print("welcome to Ye Olde Silent Auction")

more_bidders = "yes" # init main loop continue logic flag

while more_bidders == "yes":
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bids[name] = bid
    # print(bids)
    more_bidders = (input("Are there any more bids after ye? (enter 'yes' or 'no') " )).lower()
    clear()
max_bid = 0 # init bid to 0, go up from there on val tests
winner_keys = [] # store the key of current max bid, a list in case of ties
for key in bids:
    if bids[key] > max_bid:
        max_bid = bids[key]
        winner_keys = [key] # was larger, so the winners key list is replaced with the new top bidder
    elif bids[key] == max_bid:
        winner_keys.append(key) # adds a key in a tie top bid

# somewhat gracefully handle the rare tie output
if len(winner_keys) > 1:
    print(f"Top bid {max_bid} tied between " + str(len(winner_keys)) + " bidders.")
    print(", ".join(winner_keys) + ", please see the auctioneer to resolve.")
else:
    print(f"Top bid by {winner_keys[0]} with {max_bid}.")
