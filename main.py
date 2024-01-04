import time
import turtle
import snake

screen = turtle.Screen()
screen.title("Snake game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

initial_positions = [(0, 0), (-20, 0), (-40, 0)]

snake = snake.Snake()

playing = True

while playing:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


