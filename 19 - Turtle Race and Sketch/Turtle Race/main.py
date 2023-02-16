import random
from turtle import Turtle, Screen

colors = ["yellow", "orange", "red", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

all_turtles = []
x = -120
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)
    new_turtle.goto(-230, x)
    x += 50

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print("You have won!")
            else:
                print(f"You have lost! {winning_color.title()} turtle has won!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
