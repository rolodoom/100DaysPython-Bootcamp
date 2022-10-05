#######################################
# CLASS PROJECT
# Dot Art with Turtle
#######################################

# Day 18 - Dot Art with Turtle  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

from lib import random_color
from turtle import Turtle, Screen

tur = Turtle()
tur.speed("fastest")
screen = Screen()
screen.setup(520, 520)
screen.colormode(255)


def make_a_hirst():
    tur.penup()
    tur.hideturtle()
    dot_width = 20
    dot_separation = 50
    steps = 10
    screen_w = (screen.window_width() - dot_width) / 2
    xpos = (screen_w * -1) + 20
    ypos = screen_w - 20

    for i in range(steps):
        tur.goto(xpos, ypos)
        for j in range(steps):
            tur.dot(dot_width, random_color())
            tur.forward(dot_separation)
        ypos -= dot_separation


make_a_hirst()
screen.exitonclick()
