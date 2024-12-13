from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Player 1: {self.left_score}", align="center", font=("Arial", 24, "normal"))
        self.goto(100, 200)
        self.write(f"Player 2: {self.right_score}", align="center", font=("Arial", 24, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()