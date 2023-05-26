#######################################
# CLASS PROJECT
# The Snake Game
#######################################

# Day 20 - The Snake Game [Part 1] #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

# Import libraries
from turtle import Screen, Turtle
from snake import Snake
import time

# Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()

# Key Bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Exit
screen.exitonclick()
