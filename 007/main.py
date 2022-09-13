#######################################
# CLASS PROJECT
# Hangman
#######################################

# Day 7 - 🔠 Hangman Game 🔠  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

import random
from hangman_words import word_list
from hangman_art import *

# Print art
print(logo)

# Constants
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Variables
lives = 6
end_of_game = False
display = []

# Create blank display list
for _ in range(word_length):
    display.append("_")

# Main program
while not end_of_game:
    # Guess a letter
    guess = input("Guess a letter: ").lower()

    # Already pick that letter
    if guess in display:
        print(f"You've already pick letter {guess}")

    # Check if guess is correct
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Guess is not in the choosen word
    if guess not in chosen_word:
        lives -= 1
        print(f"Letter {guess} is not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print(f"The word was {chosen_word}")

    # You've guess all the letter correctly
    if not "_" in display:
        end_of_game = True
        print("You win")

    # Show the display and the hangman art
    print(" ".join(display))
    print(stages[lives])
