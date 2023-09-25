import random
import os
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
lives = 6
game_off = False
display = []

print(logo)
for letter in chosen_word:
    display.append('_')


while not game_off:
    guess = input('Guess a letter: ').lower()

    os.system('cls')

    if guess in display:
        print(f'You\'ve already guessed {guess}.')

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')

        lives -= 1
        if lives == 0:
            game_off = True
            print('You lose.')

    print(f"{' '.join(display)}")

    if '_' not in display:
        game_off = True
        print('You won!')

    print(stages[lives])
