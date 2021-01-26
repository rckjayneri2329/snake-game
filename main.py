from turtle import Turtle, Screen
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_parts = []

x_axis = 0
y_axis = 0

for i in range(3):
    snake_parts.append(Turtle(shape="square"))
    snake_parts[i].penup()
    snake_parts[i].color("white")
    snake_parts[i].goto(x=x_axis, y=y_axis)
    x_axis -= 20

screen.update()

game_is_on = True
while game_is_on:
    for part in snake_parts:
        part.forward(20)
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
