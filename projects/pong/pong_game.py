import turtle
import winsound
import time


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(1)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 2
        self.dy = 2


def setup_window():
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    return wn


def create_paddle(x, y):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, y)
    return paddle


def setup_score():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
    return pen


def update_score(pen, score_a, score_b):
    pen.clear()
    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


def paddle_a_up(paddle):
    if paddle.ycor() < 250:
        paddle.sety(paddle.ycor() + 20)


def paddle_a_down(paddle):
    if paddle.ycor() > -240:
        paddle.sety(paddle.ycor() - 20)


def paddle_b_up(paddle):
    if paddle.ycor() < 250:
        paddle.sety(paddle.ycor() + 20)


def paddle_b_down(paddle):
    if paddle.ycor() > -240:
        paddle.sety(paddle.ycor() - 20)


def check_ball_border_collision(ball):
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        play_bounce_sound()
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        play_bounce_sound()


def check_ball_paddle_collision(ball, paddle_a, paddle_b):
    if ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        play_bounce_sound()
    elif ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        play_bounce_sound()


def play_bounce_sound():
    try:
        winsound.Beep(1000, 100)
    except ImportError:
        pass


def main():
    wn = setup_window()
    paddle_a = create_paddle(-350, 0)
    paddle_b = create_paddle(350, 0)
    ball = Ball()
    pen = setup_score()

    score_a = 0
    score_b = 0

    wn.listen()
    wn.onkeypress(lambda: paddle_a_up(paddle_a), "w")
    wn.onkeypress(lambda: paddle_a_down(paddle_a), "s")
    wn.onkeypress(lambda: paddle_b_up(paddle_b), "Up")
    wn.onkeypress(lambda: paddle_b_down(paddle_b), "Down")

    while True:
        wn.update()

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        check_ball_border_collision(ball)

        check_ball_paddle_collision(ball, paddle_a, paddle_b)

        if ball.xcor() > 350:
            score_a += 1
            update_score(pen, score_a, score_b)
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1
            update_score(pen, score_a, score_b)
            ball.goto(0, 0)
            ball.dx *= -1

        ball.dx *= 1.0005  # Slight increase in X speed
        ball.dy *= 1.0005  # Slight increase in Y speed

        time.sleep(0.01)


if __name__ == "__main__":
    main()
