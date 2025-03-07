def turn_right():
    turn_left()
    turn_left()
    turn_left()

goal = False

while front_is_clear():
    move()
turn_left()
while goal != True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
    goal = at_goal()
    
done()