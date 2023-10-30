# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# tim.forward(100)
# tim.right(90)
# tim.forward(30)

# draw a square
# for i in range(4):
#    tim.forward(40)
#    tim.right(90)

# import heroes
# heroes.gen()
# print(jim)

# draw a dashed line

# for move in range(10):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

# draw different shapes, square, pentagon etc

# for angles in range(4,11):
#     angle = 360/angles
#     print(angle)
#     for side in range(angles):
#         tim.right(angle)
#         tim.forward(40)

# official solution
########### Challenge 3 - Draw Shapes ########
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


# draw a random walk
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# turn_angles = [0,90,180,270]
# tim.pensize(10)
# for move in range(100):
#     tim.color(random.choice(colors))
#     tim.forward(10)
#     tim.right(random.choice(turn_angles))

# official

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_color = (r, g, b)
    return turtle_color


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# keep this at bottom of file
screen = Screen()
screen.exitonclick()
