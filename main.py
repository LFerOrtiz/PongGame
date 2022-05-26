from scoreboard import ScoreBoard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

INIT_POSITION = [(350, 0), (-350, 0)]
game_on = True

# Setup of the screen for the game
screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
user_left = Paddle(INIT_POSITION[0])
user_right = Paddle(INIT_POSITION[1])
score = ScoreBoard()

screen.listen()
screen.onkey(user_left.move_up, key="Up")
screen.onkey(user_left.move_down, key="Down")

screen.onkey(user_right.move_up, key="w")
screen.onkey(user_right.move_down, key="s")

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detect the collision with the top and button of the window
    if ball.ycor() >= 281 or ball.ycor() <= -276:
        ball.bound_y()

    # Detect the collision with the palled
    if ball.distance(user_left) < 55 and ball.xcor() > 318:
        ball.bound_x()
        score.l_point()

    if ball.distance(user_right) < 55 and ball.xcor() < -318:
        ball.bound_x()
        score.r_point()

    # Reset the ball to the center, if it go out of the window
    if ball.xcor() >= 350 or ball.xcor() <= -350:
        ball.restart_ball()

screen.exitonclick()
