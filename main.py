import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Your Snake Game")
screen.tracer(0)


snake = Snake()

# bind arrow keys to control snake direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score_board = Scoreboard()
food = Food()
is_game_on = True
while is_game_on:
    time.sleep(0.2)
    screen.update()
    snake.move()
    #time.sleep(1)
    if snake.head.distance(food) <= 15:
        snake.extend()
        food.refresh()
        score_board.increse_score()

    # detect collision with the walls and game over!!
    if snake.head.xcor() <= -290 or snake.head.xcor() >= 290 or snake.head.ycor() <= -290 or snake.head.ycor() >= 290:
        is_game_on = False
        score_board.game_over()

    # detect collision with tail and game over
    if snake.did_snake_head_collision_with_tail():
        is_game_on = False
        score_board.game_over()

    #time.sleep(1)


screen.exitonclick()