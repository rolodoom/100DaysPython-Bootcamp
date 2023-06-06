#######################################
# CLASS PROJECT
# Pong Game
#######################################

# Day 22 - Pong Game  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp


# Import libraries
from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# Setup
# 1. Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# 2. Create and move the paddle
# 3. Create another paddle
# Create the paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# 4. Create the ball and make it move
ball = Ball()

# 8. Keep score
scoreboard = Scoreboard()

# Key Bindings
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(l_paddle.up, "W")
screen.onkey(l_paddle.down, "S")

# Main Loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # 5. Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce Y
        ball.bounce_y()

    # 6. Detect collision with paddle
    # Detect collision with r_paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        # Needs to bounce X
        ball.bounce_x()

    # 7. Detect when paddle misses
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Exit
screen.exitonclick()
