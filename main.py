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

w_brick_list = []
g_brick_list = []
r_brick_list = []


def place_bricks():
    global w_brick_list, g_brick_list, r_brick_list
    offset = 0
    for i in range(17):
        w_brick = Brick(x=-370 + offset, y=200, color="white")
        w_brick_list.append(w_brick)
        g_brick = Brick(x=-370 + offset, y=150, color="green")
        g_brick_list.append(g_brick)
        r_brick = Brick(x=-370 + offset, y=100, color="red")
        r_brick_list.append(r_brick)
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
        scoreboard.point()

    # Detect collision with brick
    for brick in w_brick_list:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            w_brick_list.remove(brick)
            brick.destroy_brick()
    for brick in g_brick_list:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            g_brick_list.remove(brick)
            brick.destroy_brick()
    for brick in r_brick_list:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            r_brick_list.remove(brick)
            brick.destroy_brick()

    if len(w_brick_list) == 0 and len(g_brick_list) == 0 and len(r_brick_list) == 0:
        games_is_on = False

screen.exitonclick()
