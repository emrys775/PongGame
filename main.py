from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Create paddles
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)

# Create ball
ball = Ball()

# Create scoreboard
scoreboard = ScoreBoard()

# Key bindings
screen.listen()
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.016)  # About 60 FPS
    screen.update()

    # Move the ball
    ball.move()

    # Detect collision with top or bottom wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.xcor() > 350 and right_paddle.distance(ball) < 50) or (
            ball.xcor() < -350 and left_paddle.distance(ball) < 50):
        ball.bounce_x()

    # Detect if the ball passes the paddles
    if ball.xcor() > 380:  # Ball passed the right paddle
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -380:  # Ball passed the left paddle
        ball.reset_position()
        scoreboard.right_point()

# Exit on close
screen.mainloop()