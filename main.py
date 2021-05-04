from turtle import Screen
from paddle import Paddle
from field import Field
from score import ScoreBoard
from ball import Ball
import time as t


scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor("black")
scr.title("Pong")
scr.tracer(0)
scr.listen()

game_end = False

player_1 = Paddle("Player_1")
player_2 = Paddle("Player_2")
field = Field()
score = ScoreBoard(scr)
ball = Ball()


def is_game_over():
    global game_end
    game_end = True


while not game_end:
    scr.update()

    scr.onkeypress(fun=is_game_over, key="e")
    scr.onkeypress(fun=player_1.move_up, key="Up")
    scr.onkeypress(fun=player_1.move_down, key="Down")

    ball.move(player_1)

    t.sleep(0.001)
