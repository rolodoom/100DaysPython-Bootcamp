#######################################
# CLASS PROJECT
#######################################

# Day 3 - The Dungeon #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

print("--------------------------------------")
print("      Welcome to the dungeon")
print("Your mission is to find the master key")
print("--------------------------------------\n")

game_over = "Game over. You loose."

choice1 = input(
    'There are two passages in front of you, which one do you want to go through, the "right" or the "left"?\n > '
).lower()

if choice1 == "left":
    choice2 = input(
        'You\'ve reached a large room with two stairs. Where do you go, "up" or "down"?\n > '
    ).lower()

    if choice2 == "up":
        choice3 = input(
            'You arrive at a new floor where there are three iron doors. Do you choose the one to your "left", "center" or "right"?\n > '
        ).lower()
        if choice3 == "center":
            print("You found the master key!\n:: Y O U   W I N ::\n")
        elif choice3 == "left":
            print("You enter the room and there's a trap that cuts your head off.")
            print(game_over)
        else:
            print("You enter the room and there's a guard that shoots you to death.")
            print(game_over)

    else:
        print(
            "You come to a room where there is a wild beast and it attacks you. You die."
        )
        print(game_over)

else:
    print("You start walking and fall down an abyss.")
    print(game_over)
