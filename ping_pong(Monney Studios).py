import turtle
import random

"""
This is a ping pong game made by Monney Joshua
"""

# display a screen with properties
window = turtle.Screen()
window.title("Ping Pong(Monney Studios)")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.goto(-350, 0)
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.goto(350, 0)
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.penup()
ball.color("white")
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

name = turtle.Turtle()
name.speed(0)
name.penup()
name.color("white")
name.goto(380, -290)
name.hideturtle()
name.write("Monney Studios", align="right", font=("Scream Real", 10, "bold"))


# paddle A move up
def paddle_a_move_up():
    a_move_up = paddle_a.ycor()
    a_move_up += 20
    paddle_a.sety(a_move_up)


# paddle A move down
def paddle_a_move_down():
    a_move_down = paddle_a.ycor()
    a_move_down += -20
    paddle_a.sety(a_move_down)


# paddle B move up
def paddle_b_move_up():
    b_move_up = paddle_b.ycor()
    b_move_up += 20
    paddle_b.sety(b_move_up)


# paddle B move down
def paddle_b_move_down():
    b_move_down = paddle_b.ycor()
    b_move_down += -20
    paddle_b.sety(b_move_down)


# paddle A and B controls
window.listen()
window.onkeypress(paddle_a_move_up, "w")
window.onkeypress(paddle_a_move_down, "s")
window.onkeypress(paddle_b_move_up, "Up")
window.onkeypress(paddle_b_move_down, "Down")

choices = [1, -1]

# scores
a_score = 0
b_score = 0

# player scores board
player_scores = turtle.Turtle()
player_scores.speed(0)
player_scores.goto(0, 240)
player_scores.color("white")
player_scores.hideturtle()
player_scores.penup()
player_scores.write(f"Player 1: {a_score}\t\t\tPlayer 2: {b_score}", align="center", font=("Courier", 16, "bold"))

# run window
while True:
    ball_position = random.choice(choices)

    # ball movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 600:
        ball.goto(0, 0)
        ball.dx *= -1
        player_scores.clear()
        ball.dy *= ball_position
        a_score += 1
        player_scores.write(f"Player 1: {a_score}\t\t\tPlayer 2: {b_score}", align="center",
                            font=("Courier", 16, "bold"))

    if ball.xcor() < -600:
        ball.goto(0, 0)
        ball.dx *= -1
        player_scores.clear()
        ball.dy *= ball_position
        b_score += 1
        player_scores.write(f"Player 1: {a_score}\t\t\tPlayer 2: {b_score}", align="center",
                            font=("Courier", 16, "bold"))

    # paddle A and B up movement limit
    if paddle_a.ycor() > 245:
        paddle_a.goto(-350, 245)

    if paddle_a.ycor() < -240:
        paddle_a.goto(-350, -240)

    if paddle_b.ycor() > 245:
        paddle_b.goto(350, 245)

    if paddle_b.ycor() < -240:
        paddle_b.goto(350, -240)

    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    window.update()
