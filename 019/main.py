#######################################
# CLASS PROJECT
# The Turtle Race
#######################################

# Day 19 - The Turtle Race  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

import random
from turtle import Turtle, Screen


is_race_on = False
screen = Screen()
screen.setup(width=420, height=420, startx=100, starty=100)
screen.bgcolor("lightgray")
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_start = 120

for turtle_index in range(0, 6):
    y_position = turtle_index * 50 - y_start
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_position)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 180:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
