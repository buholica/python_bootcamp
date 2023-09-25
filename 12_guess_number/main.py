import random
from art import logo


def difficulty_level(selected_difficulty):
    """Function to set the amount of turns depending on difficulty"""

    if selected_difficulty == "easy":
        return 10
    else:
        return 5


def guess_check(answer, user_guess):
    """Function to check user answer against actual answer"""

    if user_guess == answer:
        print(f"  You got it! The answer is {answer}.")
        return 1
    elif user_guess > answer:
        print(f"  Too high.")
        print(f"  Guess again.")
        return 0
    else:
        print(f"  Too low.")
        print(f"  Guess again.")
        return 0


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
print(f"   Pssst, the correct answer is {number}.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
print(f"  You have {difficulty_level(difficulty)} attempts remaining to guess the number.")
attempts = difficulty_level(difficulty)

end_of_game = False

while not end_of_game:
    guess = int(input("Make a guess: "))

    if guess_check(number, guess) == 1:
        end_of_game = True
    else:
        attempts -= 1
        if attempts > 0:
            if attempts == 1:
                print(f"  You have {attempts} attempt remaining to guess the number.")
            else:
                print(f"  You have {attempts} attempts remaining to guess the number.")
        elif attempts == 0:
            end_of_game = True
            print("  You lose!")
        else:
            print("  You've run out of guesses, you lose.")