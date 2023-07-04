#######################################
# CLASS PROJECT
# The Snake Game
#######################################

# Day 24.1 - The Snake Game [Part 3 - Add High Score] #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

# Import libraries
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()
scoreboard = Scoreboard()

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

    # 4. Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # 6. Detect collision with a wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -290
        or snake.head.ycor() > 280
        or snake.head.ycor() < -290
    ):
        scoreboard.reset()
        snake.reset()

    # 7. Detect a collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# Exit
screen.exitonclick()
