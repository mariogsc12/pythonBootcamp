from turtle import *
import random

colors = ["CornflowerBlue","GreenYellow", "Magenta"]

def draw_polygon(turtle: Turtle, num_sides: int, size: int):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.right(angle)

def define_style(turtle: Turtle, _color: str):
    turtle.color(_color)

def main():
    my_turtle = Turtle()
    for num_side in range(3,10):
        define_style(my_turtle, random.choice(colors))
        draw_polygon(my_turtle, num_side, 100)

if __name__ == "__main__":
    main()