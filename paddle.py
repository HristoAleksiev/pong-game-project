from turtle import Turtle

UPPER_LIMIT = 265
LOWER_LIMIT = -255


class Paddle(Turtle):

    def __init__(self, owner):
        super().__init__()

        self.paddle_owner = owner
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapetransform(1, 0, 0, 4)
        self.setheading(90)

        self.render_in_position()

    # there is a difference in the position of different paddles: player 1 ends in coord x = -360, other at x = 350
    def render_in_position(self):

        if self.paddle_owner == "Player_1":
            self.setx(-370)
            self.sety(0)
        else:
            self.setx(360)
            self.sety(0)

    def move_up(self):

        if self.position()[1] + 40 < UPPER_LIMIT:
            self.setheading(90)
            self.forward(10)

    def move_down(self):
        if self.position()[1] - 40 > LOWER_LIMIT:
            self.setheading(270)
            self.forward(10)
