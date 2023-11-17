from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 5)
        self.setheading(270)
        self.color("white")
        self.goto(position)

    def move_up(self):
        self.backward(30)

    def move_down(self):
        self.forward(30)
