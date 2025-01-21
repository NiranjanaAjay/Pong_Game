from turtle import Turtle
MOVE_DISTANCE=20

class Paddle(Turtle):
    def __init__(self,starting_position):
        super().__init__()
        self.parts=[]
        self.create_paddle(starting_position)


    def create_paddle(self,starting_position):
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(starting_position)


    def go_up(self):
        new_y=self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
