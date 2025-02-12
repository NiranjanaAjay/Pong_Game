from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",60,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score=0
        self.r_score=0
        self.writing()

    def l_point(self):
        self.l_score+=1
        self.writing()

    def r_point(self):
        self.r_score+=1
        self.writing()

    def writing(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

