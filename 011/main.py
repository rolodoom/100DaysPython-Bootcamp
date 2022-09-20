#######################################
# CLASS PROJECT
# Blackjack Capstone
#######################################

# Day 11 - 🃏 Blackjack Capstone 🃏  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

from art import *
import random
import platform
import os


def clear():
    system = platform.system().lower()
    if system == "linux" or system == "darwin":
        os.system("clear")
    elif system == "windows":
        os.system("cls")


def get_card():
    """Returns a random card from the deck"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)


def get_score(cards):
    """Calculates the score from a card list. 0 Represents the blackjack"""
    if len(cards) == 2 and sum(cards) == 21:
        # blackjack
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_scores(player1_score, player2_score):
    """Compares the scores and returns the winner"""
    if player1_score == player2_score:
        return "It's a draw!"
    elif player2_score == 0:
        return "You loose! Computer has a Blackjack!"
    elif player1_score == 0:
        return "You win with a Blackjack!"
    elif player1_score > 21:
        return f"You went over! You loose!"
    elif player2_score > 21:
        return f"Computer went over. You Win!"
    elif player1_score > player2_score:
        return f"You Win!"
    else:
        return f"You loose!"


def blackJack():

    print(logo)

    player1_cards = []
    player2_cards = []

    for _ in range(2):
        player1_cards.append(get_card())
        player2_cards.append(get_card())

    game_over = False

    while not game_over:

        player1_score = get_score(player1_cards)
        player2_score = get_score(player2_cards)
        print(f"\n  Your cards: {player1_cards}, current score: {player1_score}")
        print(f"  Computer's first card: {player2_cards[0]}")

        if player1_score > 21 or player1_score == 0 or player2_score == 0:
            game_over = True
        else:
            player1_deal = input("\nGet another card? [y/n]: ").lower()
            if player1_deal == "y":
                player1_cards.append(get_card())
            else:
                game_over = True

    while player2_score != 0 and player2_score < 17:
        player2_cards.append(get_card())
        player2_score = get_score(player2_cards)

    print(f"\n- Your final cards: {player1_cards}, final core: {player1_score}")
    print(f"- Computer's final cards: {player2_cards}, final score: {player2_score}")
    print(f"\n{compare_scores(player1_score, player2_score)}")


while input("\nDo you want to play Blackjack? [y/n]: ").lower() == "y":
    clear()
    blackJack()

print("Bye! :)")
