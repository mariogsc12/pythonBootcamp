from turtle import *
import random

colors = ["CornflowerBlue", "Magenta", "Black", "Tomato"]
directions = [0, 90, 180, 270]

running = True  # Flag used to continue drawing

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

def draw_spirograph(turtle: Turtle, radius: int, offset: int):
    turtle.circle(radius)
    turtle.setheading(offset)


def stop_drawing(x, y):
    global running
    running = False

def main():
    # Flag to end the loop
    global running

    # Objects
    my_turtle = Turtle()
    screen = Screen()

    # Configuration
    screen.onclick(stop_drawing)
    max_steps = 200
    prev_offset = 0
    offset = 10
    pensize = 3

    # Main loop
    step = 0
    while running and step < max_steps:
        define_style(my_turtle, "random", pensize)
        radius = random.randint(100,120)
        prev_offset += offset
        draw_spirograph(my_turtle,radius,prev_offset)
        step += 1

    # Close the screen after the loop
    screen.bye()

if __name__ == "__main__":
    main()
