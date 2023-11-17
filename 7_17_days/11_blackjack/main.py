import random
import os
from art import logo


def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    sum = 0
    for card in cards:
        sum += card

    if sum == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum > 21:
        cards.remove(11)
        cards.append(1)
    return sum


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def game():
    print(logo)

    user_cards = []
    computer_cards = []
    end_of_game = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not end_of_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'    User cards are {user_cards}, and user score is {user_score}.')
        print(f'    PC first card is {computer_cards[0]}.')

        if computer_score == 0 or user_score == 0 or user_score > 21:
            end_of_game = True
        else:
            another_card = input("Do you want to draw another card? Type 'yes' or 'no'. ").lower()
            if another_card == 'yes':
                user_cards.append(deal_card())
            else:
                end_of_game = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Your final hand: {user_cards}, final score: {user_score}.")
    print(f"  PC final hand: {computer_cards}, final score: {computer_score}.")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'yes' or 'no'. ").lower() == "yes":
    os.system('cls')
    game()