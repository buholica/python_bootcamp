import random
import turtle

timmy = turtle.Turtle()
turtle.colormode(255)
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
ycor = -225
timmy.setx(-230)
timmy.sety(ycor)

rgb_colors =[]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for item in range(15):
    random_color()
    rgb_colors.append(random_color())


def print_row():
    for _ in range(10):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.forward(50)


for _ in range(10):
    print_row()
    timmy.setx(-230)
    ycor += 50
    timmy.sety(ycor)


screen = turtle.Screen()
screen.exitonclick()