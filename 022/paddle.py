# Paddle class
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.goto(position)

    # Move the Paddle
    def up(self):
        new_y = self.ycor() + 20
        if new_y < 280:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        if new_y > -260:
            self.goto(self.xcor(), new_y)
