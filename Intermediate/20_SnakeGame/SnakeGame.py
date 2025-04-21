from turtle import Screen, Turtle
import time
import random

# --- Configuration parameters ---
# Snake
DISTANCE = 20
INITIAL_SEGMENTS = 3
# Screen
SCREEN_SIZE = 600
SCREEN_FOOD_LIMITS = 50
# Food
FOOD_SIZE = 0.5
# Screenboard
SCREENBOARD_ALIGMENT = "center"
SCREENBOARD_FONT = ("Arial",24,"normal")
SCREENBOARD_POSITION = 0,260
# Game logic
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class CustomSnake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self,position=(0,0)):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        return new_segment
    
    def create_snake(self):
        self.segments.append(self.add_segment())
        for i in range(1, INITIAL_SEGMENTS):
            self.segments.append(self.add_segment(self.segments[-1].position()))

    def increase_size(self):
        self.segments.append(self.add_segment(self.segments[-1].position()))

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

class Food(Turtle):
    limit = int(SCREEN_SIZE/2 - SCREEN_FOOD_LIMITS)

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=FOOD_SIZE,stretch_wid=FOOD_SIZE)
        self.speed("fastest")
        self.move()

    def move(self):
        position_x = random.randint(-self.limit, self.limit)
        position_y = random.randint(-self.limit, self.limit)
        self.goto(position_x, position_y)

class ScreenMessage(Turtle):
    def __init__(self, message, position=(0,0)):
        super().__init__()
        self.visible = False
        self.message = message
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_message()

    def update_message(self):
        self.write(f"{self.message}", align=SCREENBOARD_ALIGMENT, font=SCREENBOARD_FONT)


class Scoreboard(ScreenMessage):
    def __init__(self):
        self.score = 0
        super().__init__(self.create_message(),SCREENBOARD_POSITION)

    def create_message(self):
        return f"Score: {self.score}"
    
    def update_message(self):
        self.message = self.create_message()
        super().update_message()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_message()


screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  

snake = CustomSnake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < DISTANCE:
        food.move()
        scoreboard.increase_score()
        snake.increase_size()
    
    # Detect collision with walls
    if snake.head.xcor() <= -SCREEN_SIZE/2 or snake.head.xcor() >= SCREEN_SIZE/2 or snake.head.ycor() <= -SCREEN_SIZE/2 or snake.head.ycor() >= SCREEN_SIZE/2:
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < DISTANCE/2:
            game_is_on = False

end_message = ScreenMessage("Game over")
screen.exitonclick()
