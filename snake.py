import turtle

INITIAL_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create()
        self.head = self.snake_body[0]

    def create(self):
        for position in INITIAL_POS:
            new_turtle = turtle.Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.snake_body.append(new_turtle)

    def move(self):
        for piece in range(len(self.snake_body) - 1, 0, -1):
            x_cor = self.snake_body[piece - 1].xcor()
            y_cor = self.snake_body[piece - 1].ycor()
            self.snake_body[piece].goto(x_cor, y_cor)

        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)
