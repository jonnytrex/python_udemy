def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == 0:
    if front_is_clear() != 0:
        move()
    elif wall_in_front() != 0:
        jump()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else: 
#         move()