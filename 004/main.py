#######################################
# CLASS PROJECT
#######################################

# Day 4 - Rock Paper Scissors #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp
# Public Gist
# https://gist.github.com/rolodoom/0a05559ce0356c0f5302fd2d8635f860

import random

print("--------------------------------------")
print("      Rock Paper Scissors")
print("--------------------------------------\n")

rock = "ROCK"
paper = "PAPER"
scissors = "SCISSORS"

game_items = [rock, paper, scissors]
win_msg = "You Win 🏆"
lose_msg = "You Lose 💣"
draw_msg = "It's a draw 🤝"

user = int(input("What do you choose? 0 Rock, 1 Paper, 2 Scissors:\n"))
computer = random.randint(0, 2)

if user >= 3 or user < 0:
    print(f"\nWrong number! {lose_msg}")
else:

    print(f"\nYou chose:\n{game_items[user]}\n")
    print(f"Computer chose:\n{game_items[computer]}\n")

    if (user == 0 and computer == 2) or (computer < user):
        print(win_msg)
    elif (user == 2 and computer == 0) or (computer > user):
        print(lose_msg)
    elif computer == user:
        print(draw_msg)
