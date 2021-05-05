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
        self.set_ball_position()
        self.ball.speed(self.ball_speed)

    def set_ball_position(self):
        self.ball.setx(0)
        self.ball.sety(r.randint(-150, 160))
        self.ball.setheading(r.choice([r.randint(0, 45), r.randint(315, 360), r.randint(135, 225)]))

    def move(self, player, other_player, score):
        self.detect_collision(player, other_player, score)
        self.ball.forward(self.ball_speed)

    def increase_speed(self):
        self.ball_speed = 7

    def detect_collision(self, player, other_player, score):
        current_heading = self.ball.heading()

        # The coordinate system works with negative integers as well (ex. -20: 360 - 20 = 340ª)  !!
        # Checking if the ball is hitting the top and lower walls and bouncing off of them.
        # Bouncing changes the direction the ball is heading by changing the heading in angle degrees.
        if self.ball.position()[1] + 5 >= UPPER_LIMIT or self.ball.position()[1] - 5 <= LOWER_LIMIT:
            self.ball.setheading(-current_heading)

        # Check if ball is hitting the left paddle - player 1
        if self.ball.position()[0] - 5 <= LEFT_LIMIT and \
                player.position()[1] + 40 >= self.ball.position()[1] >= player.position()[1] - 40:
            self.ball.setheading(180 - current_heading)
            self.increase_speed()

        # Check if ball is hitting the right paddle - player 2 / Computer
        if self.ball.position()[0] + 5 >= RIGHT_LIMIT and \
                other_player.position()[1] + 40 >= self.ball.position()[1] >= other_player.position()[1] - 40:
            self.ball.setheading(180 - current_heading)
            self.increase_speed()

        # Check if the ball has missed to collide with a paddle and a point has been scored.
        # Done through collision check against the back of the paddles - their X positions.
        if self.ball.position()[0] + 5 >= RIGHT_LIMIT + 20:
            self.set_ball_position()
            self.ball_speed = 5
            score_increase = score.left_score + 1
            score.update_score(score_increase, score.right_score)
        elif self.ball.position()[0] - 5 <= LEFT_LIMIT - 20:
            self.set_ball_position()
            self.ball_speed = 5
            score_increase = score.right_score + 1
            score.update_score(score.left_score, score_increase)
