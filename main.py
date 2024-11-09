from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game.")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
game_is_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    # detect collision with food
    for segment in snake.segments:
        if segment == snake.segments[1::]:
            game_is_on = False
            score.game_over()


    # detect the collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280:
        score.reset()
        snake.reset()
        score.update_score()
        score.game_over()
        game_is_on = False




    elif snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < - 280:
        score.reset()
        snake.reset()
        score.update_score()
        score.game_over()
        game_is_on = False


        # detect collision with food
    else:
        if snake.segments[0].distance(food) < 15:
            food.refresh()
            score.clear()
            snake.extend()
            score.increase_score()
            score.update_score()




screen.exitonclick()
