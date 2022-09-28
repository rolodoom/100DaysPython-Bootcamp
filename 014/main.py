#######################################
# CLASS PROJECT
# Higher Lower Game
#######################################

# Day 14 - Higher Lower Game  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

from art import *
from game_data import *
import random
import platform
import os


def clear():
    system = platform.system().lower()
    if system == "linux" or system == "darwin":
        os.system("clear")
    elif system == "windows":
        os.system("cls")


def format_account(account):
    """Takes account data ant returns printable format"""
    return f"{account['name']}, {account['description']}, from {account['country']}."


def check_guess(guess, account_a, account_b):
    """Takes guess and two accounts, and returns if the guess is right"""
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display logo
clear()
print(logo)

# Initialize variables
score = 0
end_game = False
accountB = random.choice(data)

# Make the game repetable
while not end_game:

    # Generate random account info from game data
    # Make account at position B  become next account at position A
    accountA = accountB
    accountB = random.choice(data)
    while accountA == accountB:
        accountB = random.choice(data)

    # Format the account data
    print(f"Compare A: {format_account(accountA)}")
    print(vs)
    print(f"Against B: {format_account(accountB)}")

    # Ask user for a guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follower count of each account
    ## check if user is correct
    correct_guess = check_guess(
        guess=user_guess, account_a=accountA, account_b=accountB
    )

    # Clear screen between rounds
    clear()
    print(logo)

    # Give user feedback on their guess
    ## Score keeping
    if correct_guess:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        if input("Do you want to play again? type 'Y' or 'N': ").lower() == "n":
            end_game = True
        else:
            clear()
            print(logo)

clear()
