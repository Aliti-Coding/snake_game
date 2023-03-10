from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0) #turns off what the program is doing. Therefor we call update

snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.Up, key="Up")
screen.onkey(snake.Left,key="Left")
screen.onkey(snake.Right, key="Right")
screen.onkey(snake.Down,key="Down")
screen.listen()





game_is_on = True
while game_is_on:
    
    screen.update() #updates the screen after motion
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    
    for snake_pos in snake.segments[1:]:
        if snake.head.distance(snake_pos) < 5:
            game_is_on = False
            score.game_over()
    


screen.exitonclick()