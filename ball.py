from turtle import Turtle
import random as r

UPPER_LIMIT = 265
LOWER_LIMIT = -255
RIGHT_LIMIT = 350
LEFT_LIMIT = -360


class Ball:
    ball_speed = 5

    def __init__(self):
        self.ball = Turtle()

        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.shapesize(stretch_wid=0.5)

        self.ball.sety(r.randint(-150, 160))
        # self.ball.setheading(r.choice([r.randint(0, 45), r.randint(315, 360), r.randint(135, 225)]))
        self.ball.setheading(115)
        self.ball.speed(0.5)

    def move(self, paddle):
        self.detect_collision(paddle)
        self.ball.forward(self.ball_speed)

    def increase_speed(self):
        self.ball_speed = 7

    def detect_collision(self, paddle):
        current_heading = self.ball.heading()

        if self.ball.position()[1] + 5 > UPPER_LIMIT or self.ball.position()[1] - 5 < LOWER_LIMIT:
            self.ball.setheading(360 - current_heading)

        if self.ball.position()[0] + 5 > RIGHT_LIMIT or self.ball.position()[0] - 5 < LEFT_LIMIT:
            # if paddle.position()[1] + 40 < self.ball.position()[0] > paddle.position()[1] - 40:
            if (0 < current_heading < 90) or (180 < current_heading < 270):
                self.ball.setheading(90 + current_heading)
            else:
                self.ball.setheading(360 - current_heading)
