from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)  # Paddle size is 20px by 100px
        self.penup()
        self.goto(x_pos, y_pos)

    def go_up(self):
        if self.ycor() < 240:  # Prevent paddle from going out of bounds
            self.sety(self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -240:  # Prevent paddle from going out of bounds
            self.sety(self.ycor() - 20)