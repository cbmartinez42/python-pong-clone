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

game_on = True
while game_on:
    time.sleep(.1)
    screen.update()
    ball.move()
    if ball.ycor() == 290 or ball.ycor() == -290 or ball.xcor() == player_1.xcor() or ball.xcor() == player_2.xcor():
        ball.bounce()
    elif ball.xcor() == 290:
        print('player 1 scores')
    elif ball.xcor() == -290:
        print('player 2 scores')

screen.exitonclick()
