from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("white")
        self.penup()

    def move(self):
        x_cor = self.xcor() + 10
        y_cor = self.ycor() + 10
        self.goto(x_cor, y_cor)
