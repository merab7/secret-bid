from art import logo
import sys
import os

list_of_bids = []
dict_of_users = {}
print(logo)

def clear():
    os.system( 'cls' )


def secret_bid():
    global list_of_bids
    global dict_of_users
    
    
    name = input("\nPlease enter your name: ").lower()
    bid = input("\nPlease enter your bid: $")

    try:
        bid = int(bid)
    except ValueError:
        print("Please enter a valid integer bid.")
        return secret_bid()
     
    dict_of_users[name] = bid
    list_of_bids.append(bid)

    def ending () :
        is_there_anyone = input("\nIf there is anyone willing to bid, press Y, or press X to exit: ").lower()

        if is_there_anyone == "y":
            clear()
            return secret_bid()
        elif is_there_anyone == "x":
            max_bid = max(list_of_bids)
            winner = {user:bid for user, bid in dict_of_users.items() if bid == max_bid}

            for user, bid in winner.items():
                print(f"Winner is: {user} with a bid of ${bid}")

              
        else :
            print("You have only to option Y or X please check your spelling")
            ending()
    ending()
    sys.exit()
secret_bid()
