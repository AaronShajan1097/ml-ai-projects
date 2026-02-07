from secret_auction_art import logo
import os

bids = {}
is_true = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print(logo)
print("Welcome to the secret auction program.")

while is_true:

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bids[name] = bid

    other_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bid == 'no':
        is_true = False
        find_highest_bidder(bidding_record=bids)
    elif other_bid == 'yes':
        clear = lambda: os.system('cls')
        clear()

