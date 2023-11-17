from art import logo
import os

print(logo)
bidders = {}
end = False


def find_highest_bid(bids_data):
    winner = ''
    max_bid = 0
    for person in bids_data:
        if bids_data[person] > max_bid:
            winner = person
            max_bid = bids_data[person]
    print(f'The winner is {winner} with a bid of ${max_bid}.')


while not end:
    name = input('What is your name? ')
    bid = int(input('What is your bid? $'))
    bidders[name] = bid
    #print(bidders)
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if other_bidders == 'no':
        end = True
        find_highest_bid(bidders)
    elif other_bidders == 'yes':
        os.system('cls')

