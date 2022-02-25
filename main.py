from turtle import *
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(player_2.go_up, "Up")
screen.onkey(player_2.go_down, "Down")
screen.onkey(player_1.go_up, "w")
screen.onkey(player_1.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()

screen.exitonclick()
