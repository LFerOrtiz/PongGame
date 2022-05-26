from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, init_position):
        super().__init__()

        """ Create a new paddle """
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.goto(init_position)
        self.color("white")

    def move_up(self):
        """ Move the paddle up """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """ Move the paddle down """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
