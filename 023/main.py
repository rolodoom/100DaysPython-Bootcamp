#######################################
# CLASS PROJECT
# The Turtle Crossing
#######################################

# Day 23 - The Turtle Crossing  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

# Import libraries
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

# Instances
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Key Bindings
screen.listen()
screen.onkey(player.up, "Up")

# Main Loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # 3. Detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # 4. Detect when the turtle reaches the other side
    if player.is_at_finish_line():
        scoreboard.increase_score()
        player.go_to_start()
        car_manager.level_up()


# Exit
screen.exitonclick()
