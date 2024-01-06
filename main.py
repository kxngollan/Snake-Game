import time
import turtle
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.title("Snake game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

playing = True

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while playing:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.add()



