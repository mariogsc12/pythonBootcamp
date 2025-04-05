from turtle import *
import random

colors = ["CornflowerBlue", "Magenta", "Black", "Tomato"]
directions = [0, 90, 180, 270]

def draw_random_walk(turtle: Turtle, direction: int, size: int):
    turtle.forward(size)
    turtle.setheading(direction)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def define_style(turtle: Turtle, _color: str, _pensize: int):
    if _color == "random":
        colormode(255)
        new_color = random_color()
    elif _color in colors:
        new_color = _color
    else: 
        new_color = "Black"

    turtle.color(new_color)
    turtle.pensize(_pensize)
    turtle.speed("fastest")

def main():
    my_turtle = Turtle()
    max_steps = 500
    min_size = 20
    max_size = 50
    for num_side in range(0,max_steps):
        define_style(my_turtle, "random", 5)
        draw_random_walk(my_turtle, random.choice(directions), random.randint(min_size, max_size))

if __name__ == "__main__":
    main()