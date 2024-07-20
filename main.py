import turtle as t
from snake import Snake
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)

screen.title('Snake Game')
screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.show_scoreboard()

snake = Snake()

is_playing = True

while is_playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    screen.listen()
    screen.onkey(key='Up', fun=snake.up)
    screen.onkey(key='Down', fun=snake.down)
    screen.onkey(key='Left', fun=snake.left)
    screen.onkey(key='Right', fun=snake.right)

    screen.onkey(key='w', fun=snake.up)
    screen.onkey(key='s', fun=snake.down)
    screen.onkey(key='a', fun=snake.left)
    screen.onkey(key='d', fun=snake.right)


screen.exitonclick()
