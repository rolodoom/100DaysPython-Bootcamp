#######################################
# CLASS PROJECT
# Secret Bid
#######################################

# Day 9 - Secret Bid  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

from auction_data import *

print(logo)
print("Wecome to the secret bid program.")

bidders = {}
exit_program = False


def find_highest_bidder(bidding_dictionary):
    winner_name = ""
    winner_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > winner_bid:
            winner_name = bidder
            winner_bid = bid_amount

    print(f"\nThe winner is {winner_name} with a bid of ${winner_bid}")


while not exit_program:

    name = input("\nWhat is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if continue_bid == "no":
        exit_program = True


find_highest_bidder(bidders)
