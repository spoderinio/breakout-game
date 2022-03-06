from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard
from brick import Brick


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -280))

ball = Ball((0, -270))
scoreboard = Scoreboard()

brick_list = []


def place_bricks():
    global brick_list
    offset = 0
    for i in range(17):
        w_brick = Brick(x=-370 + offset, y=200, color="white")
        brick_list.append(w_brick)
        g_brick = Brick(x=-370 + offset, y=150, color="green")
        brick_list.append(g_brick)
        r_brick = Brick(x=-370 + offset, y=100, color="red")
        brick_list.append(r_brick)
        offset += 45


place_bricks()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

games_is_on = True
while games_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280:
        ball.bounce_y()

    elif ball.xcor() > 360 or ball.xcor() < -360:
        ball.bounce_x()

    # detect collision with paddles
    elif ball.distance(paddle) < 60 and ball.ycor() < -260:
        ball.bounce_y()

    # Detect if paddle misses the ball

    elif ball.ycor() < -290:
        ball.reset_position(paddle.position() + (0, 20))

    # Detect collision with brick
    for brick in brick_list:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            brick_list.remove(brick)
            brick.destroy_brick()
            scoreboard.point()

    if len(brick_list) == 0:
        games_is_on = False

screen.exitonclick()
