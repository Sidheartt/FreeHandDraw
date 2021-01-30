from turtle import Turtle, Screen
import random
race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Which turtle will win ?", "Color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all = []

for turt in range(0, 6):
    new = Turtle(shape="turtle")
    new.color(colors[turt])
    new.penup()
    new.goto(-240, y_pos[turt])
    all.append(new)

if user_bet:
    race_on = True

while race_on:
    for turtle in all:
        if turtle.xcor() > 230:
            race_on = False
            won = turtle.pencolor()
            if won == user_bet:
                print("You won")
            else:
                print(f"You Lose,The {won} turtle Won")

        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
