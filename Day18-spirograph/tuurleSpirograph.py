import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

# create a spirograph:
#   * draw a circle at a starting point
#   * tilt the circle a little and repeat all the way around use turtle.tilt

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_color = (r, g, b)
    return turtle_color

# draw a circle use turtle.circle
tim.pensize(1)
tim.speed("fastest")
#tim.circle(50)

#official answer:
# current_heading = tim.heading()

def draw_spirograph(size_of_gap):

    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

# keep this at bottom of file
screen = t.Screen()
screen.exitonclick()
