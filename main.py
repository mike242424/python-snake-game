import turtle as t
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = t.Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.show_scoreboard()

snake = Snake()
food = Food()

is_playing = True
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

screen.onkey(key='w', fun=snake.up)
screen.onkey(key='s', fun=snake.down)
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='d', fun=snake.right)

while is_playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.add_one()
        food.change_position()


screen.exitonclick()
