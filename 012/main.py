#######################################
# CLASS PROJECT
# Guessing Number
#######################################

# Day 12 - ❓Guessing Number Game❓  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

from art import *
from random import randint
import platform
import os


def set_difficulty(letter):
    difficulty = {
        "e": 15,
        "m": 10,
        "h": 5,
    }
    return difficulty[letter]


def clear():
    system = platform.system().lower()
    if system == "linux" or system == "darwin":
        os.system("clear")
    elif system == "windows":
        os.system("cls")


def guess_number():

    end_game = False

    while not end_game:
        clear()
        print(logo)

        magic_number = randint(1, 100)
        user_choose = input(
            "Choose a difficulty.\n ┕[E]asy\n ┕[M]edium\n ┕[H]ard\n[Q]uit\n\nCommands [E,M,H,Q]: "
        ).lower()

        if user_choose != "q":

            attempts = set_difficulty(user_choose)

            # Guess Loop
            winner = False
            while attempts > 0 and winner == False:
                user_guess = int(
                    input(
                        f"\nYou have {attempts} attempts remaining...\n━ Make a guess: "
                    )
                )
                if user_guess == magic_number:
                    winner = True
                elif user_guess < magic_number:
                    print("  └─Too low.")
                    attempts -= 1
                else:
                    print("  └─Too high.")
                    attempts -= 1

            if winner:
                print("\n🎉 You Win 🎉")
            else:
                print(f"\n💥 You loose 💥 The number was {magic_number}!")

            if input("\nDo you want to play again? [y/n]: ").lower() == "y":
                guess_number()
            else:
                end_game = True

        else:
            end_game = True


guess_number()

clear()
