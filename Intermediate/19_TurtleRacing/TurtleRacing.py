from turtle import Turtle, Screen
import random


screen_width = 500
screen_height = 400
screen_margin_y = 50
screen_margin_x = 50

start_point_x = -(screen_width-screen_margin_x)/2
end_point_x = (screen_width-screen_margin_x)/2

max_turtles = 7
min_turtles = 2
max_distance = 10

colors = ["red", "orange", "yellow","green","blue","purple","gray"]

class CustomTurtle(Turtle):
    def __init__(self, start_point:tuple, _color):
        self.my_color = _color
        
        super().__init__(shape="turtle")
        self.penup()
        self.goto(x=start_point[0], y=start_point[1])    
        self.color(self.my_color)
        

def main():
    # Create objects
    screen = Screen()
    screen.setup(width=500,height=400)

    # User input to define the number of turtles and the bet
    try:

        nb_turtles = 0
        while nb_turtles not in range(min_turtles,max_turtles):
            nb_turtles = int(screen.textinput(title="user input", prompt="Introduce the number of turtles for the race"))

        user_bet = ""
        while user_bet not in colors[0:nb_turtles]:
            user_bet = screen.textinput(title="user input 2", prompt=f"Introduce your bet {colors[0:nb_turtles]}")

        is_race_on = True
    except ValueError:
        print(f"Invalid value, please introduce a number")
        return
    
    all_turtles = []

    for turtle_index in range(0,nb_turtles):
        start_point_y = calculate_start_point_y(nb_turtles,turtle_index,screen_height,screen_margin_y)
        all_turtles.append(CustomTurtle((start_point_x, start_point_y), colors[turtle_index]))

    while is_race_on:
        for turtle in all_turtles:
            rand_distance = random.randint(0,max_distance)
            turtle.forward(rand_distance)
            
            if turtle.xcor() > end_point_x:
                winner = turtle
                is_race_on = False

    if user_bet == winner.my_color:
        print(f"You have won! The winner is the {winner.my_color} turtle")
    else:
        print(f"You have lost! The winner is the {winner.my_color} turtle")

    # Close the screen after the loop
    screen.exitonclick()


def calculate_start_point_y(nb_turtles, turtle_index, screen_height, screen_margin_y):
    start_offset_y = (screen_height-screen_margin_y)/nb_turtles
    start_point_y = start_offset_y * (turtle_index + 1)

    return start_point_y - (screen_height/2)

if __name__ == "__main__":
    main()