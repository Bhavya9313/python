import os

def find_winner(bidder_details):   #boby:30000,shiyam:50000,ram:70000
    highest_bid = 0
    winner = ""

    for bidder in bidder_details:  #bidder=boby
        bidding_price = bidder_details[bidder]

        if bidding_price>highest_bid:
            highest_bid = bidding_price
            winner = bidder

    print(f"list of all the bidders {bidder_details}")
    print(f"the winnner is {winner} with a bid price of {highest_bid}")

bidder_data = {} #bid means 'nilami me boli lagana

while True:
    name = input("what is your name")
    price = int(input("what is yor bid:"))
    bidder_data[name]=price
    more_bidder = input("are there more bidders? type 'yes' or 'no'").lower()

    if more_bidder =="no":
        find_winner(bidder_data)
        break 

    elif more_bidder == "yes":
        os.system("cls")  # to clear the screen