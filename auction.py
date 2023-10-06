# Secret Auction Program
import os
print("Welcome to Secret Auction Program.")
bidders = {}
bidding_completed = False
def highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Congratulations! {winner} won the auction with the highest bid of: ${highest_bid}")

while not bidding_completed:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    new_bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if new_bid == "no":
        bidding_completed = True
        highest_bidder(bidders)
    elif new_bid == "yes":
        os.system('clear')
    else:
        print("Please enter a valid option")
        exit()
