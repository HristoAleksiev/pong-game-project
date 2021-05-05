from turtle import Turtle


class Field:
    upper_line = Turtle()
    lower_line = Turtle()

    def __init__(self):
        self.middle_line = Turtle()

        # upper line ends at coordinate X = 265
        self.upper_line.sety(285)

        self.upper_line.penup()
        self.upper_line.shape("square")
        self.upper_line.color("white")
        self.upper_line.shapetransform(1, 0, 0, 39)

        # lower line ends at coordinate X = -255
        self.lower_line.sety(-275)

        self.lower_line.penup()
        self.lower_line.shape("square")
        self.lower_line.color("white")
        self.lower_line.shapetransform(1, 0, 0, 39)

        # dotted line in the middle is drawn; upper and lower lines are objects, they will be needed for collision

        self.middle_line.shape("square")
        self.middle_line.color("white")
        self.middle_line.setheading(270)
        self.middle_line.penup()
        self.middle_line.hideturtle()
        self.middle_line.pensize(5)

        middle_line_y = 265
        self.middle_line.sety(middle_line_y)

        for _ in range(18):
            self.middle_line.pendown()
            self.middle_line.forward(10)
            self.middle_line.penup()
            self.middle_line.forward(20)
