from turtle import *


class Paddle(Turtle):
    def __init__(self, player_num):
        paddle = Turtle()
        paddle.shape('square')
        paddle.color('white')
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        if player_num == '1':
            paddle.goto(-350, 0)
        else:
            paddle.goto(350, 0)
        
    
        
        