import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")

bids = {}
while True:



    name = input("What is your name? ")
    bid = input("What is your bid? $")

    bids[name] = bid
    print("Are there any other bidders? Type 'yes' or 'no'.")

    if input().lower() == "yes":
        clear()
    else:
        highest_bid = 0
        winner = ""
        for bidder in bids:
            bid_amount = int(bids[bidder])
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}.")    
        break