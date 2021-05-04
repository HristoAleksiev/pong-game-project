from turtle import Turtle, Screen


class ScoreBoard:
    left_score = 0
    right_score = 0

    def __init__(self, screen):

        self.writer = Turtle()
        self.writer.penup()
        self.writer.hideturtle()
        self.writer.color("white")
        self.writer.sety(170)

        self.writer.setx(-140)
        self.writer.write(arg=self.left_score, font=("Arial", 70, "normal"))

        self.writer.setx(90)
        self.writer.write(arg=self.right_score, font=("Arial", 70, "normal"))

    def update_score(self, left_score, right_score):
        self.left_score = left_score
        self.right_score = right_score
