from art import logo, vs
from game_data import data
import random
import os

#SCORE = 0


def format_data(variant):
    """Format the variant data into printable format."""
    variant_name = variant["name"]
    variant_desc = variant_a["description"]
    variant_country = variant["country"]
    return f"{variant_name}, a {variant_desc}, from {variant_country}."


def check_user_answer(guess, followers_a, followers_b):
    """Check if user's guess is correct"""
    # global SCORE
    # if guess == 'a' and num_a > num_b:
    #     SCORE += 1
    #     print(f"You are right! Your score is {SCORE}.")
    #     return 1
    # elif guess == 'b' and num_b > num_a:
    #     #SCORE += 1
    #     print(f"You are right! Your score is {SCORE}.")
    #     return 2
    # else:
    #     #os.system('cls')
    #     #print(f"Sorry, that's wrong. Final score: {SCORE}.")
    #     return 0
    if followers_a > followers_b:
        return guess == "a"
    else:
        return guess == "b"


# def setting_variant_a(right_answer, var_a, var_b):
#     if right_answer == 1:
#         return var_b
#     elif right_answer == 2:
#         return var_a


print(logo)
end_of_game = False
score = 0
variant_b = random.choice(data)

while not end_of_game:
    variant_a = variant_b
    variant_b = random.choice(data)
    while variant_b == variant_a:
        variant_b = random.choice(data)

    print(f"   Compare A: {format_data(variant_a)}")
    print(vs)
    print(f"   Against B: {format_data(variant_b)}")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_user_answer(user_guess, variant_a['follower_count'], variant_b['follower_count'])

    os.system('cls')

    if is_correct:
        score += 1
        print(f"You are right! Your current score is {score}.")
    else:
        end_of_game = True
        print(f"Sorry, that's wrong. Final score: {score}.")

    #variant_a = setting_variant_a(is_correct, variant_a, variant_b)

    # if is_correct == 0:
    #     end_of_game = True