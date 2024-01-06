import turtle

SCORE = 0


class Scoreboard():
    def __init__(self):
        self.score = f"Score: {SCORE}"
        self.scoreboard = turtle.Turtle()
        self.scoreboard.color("white")
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(0, 270)
        self.scoreboard.write(self.score, align="center", font=("Courier", 24, "normal"))

    def add(self):
        global SCORE
        SCORE += 10
        self.scoreboard.clear()
        self.score = f"Score: {SCORE}"
        self.scoreboard.write(self.score, align="center", font=("Courier", 24, "normal"))
