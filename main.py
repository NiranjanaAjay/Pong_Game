from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

STARTING_POSITION_RIGHT=(360,0)
STARTING_POSITION_LEFT=(-360,0)

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_paddle= Paddle(STARTING_POSITION_LEFT)
r_paddle=Paddle(STARTING_POSITION_RIGHT)

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

ball=Ball()
scoreboard=Scoreboard()

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detection of collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with the paddle
    if (ball.xcor()>340 and ball.distance(r_paddle)<50) or (ball.xcor()<-340 and ball.distance(l_paddle)<50):
        ball.bounce_x()

    #ball misses r paddle
    if ball.xcor() > 390 :
        ball.reset_position()
        scoreboard.l_point()

    # ball misses l paddle
    if ball.xcor() < -390 :
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()