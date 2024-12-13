from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = 3  # Initial horizontal movement speed
        self.y_move = 3  # Initial vertical movement speed
        self.speed_increment = 0.5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = -self.y_move

    def bounce_x(self):
        self.x_move = -self.x_move
        self.x_move += self.speed_increment if self.x_move > 0 else -self.speed_increment
        self.y_move += self.speed_increment if self.y_move > 0 else -self.speed_increment

    def reset_position(self):
        self.goto(0, 0)
        self.x_move = 3 if self.x_move > 0 else -3
        self.y_move = 3 if self.y_move > 0 else -3
        self.bounce_x()