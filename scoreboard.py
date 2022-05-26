from turtle import Turtle
ALIGNMENT = "center"
NORMAL_FONT = ("Bauhaus 93", 16, "normal")
BIG_FONT = ("Bauhaus 93", 22, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        """ Update the scoreboard """
        self.clear()
        self.goto(x=100, y=268)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=NORMAL_FONT)
        self.goto(x=-100, y=268)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=NORMAL_FONT)
        self.goto(x=0, y=268)
        self.write("Score", align=ALIGNMENT, font=BIG_FONT)

    def l_point(self):
        """ Add a point to the left player """
        self.l_score += 1
        self.update()

    def r_point(self):
        """ Add a point to the right player """
        self.r_score += 1
        self.update()

