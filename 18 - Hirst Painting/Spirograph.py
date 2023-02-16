import random
import turtle
from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
# timmy.shape("turtle")
turtle.colormode(255)

timmy.speed("fastest")


def colors():
    r = choice(range(0, 255))
    g = choice(range(0, 255))
    b = choice(range(0, 255))
    return r, g, b


for _ in range(360//5):

    timmy.pencolor((colors()))
    timmy.color((colors()))

    timmy.circle(100)
    timmy.setheading(timmy.heading() + 5)


screen = Screen()
screen.exitonclick()
