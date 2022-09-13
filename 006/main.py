#######################################
# CLASS PROJECT
# Get out of Reeborg's World Maze
# Always look for the right to get out of the maze
#######################################

# Day 6 - 🤖 Get out of Reeborg's World Maze 🤖 #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

from reeborg_functions import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
