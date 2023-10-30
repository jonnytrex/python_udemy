#print a list of all colors in an iamge
# each image should have a tuple of rgb
# install colorgram

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

# paint a 10 x 10 row of spots painting
# each dot 20 in size
# spacin is 50
import random
import turtle as t
screen = t.Screen()
timmy = t.Turtle()
screen.colormode(255)

# set timmy's starting position
timmy.penup()
x = -335
y = -285
timmy.setx(x)
timmy.sety(y)

#timmy.dot(20,(132, 166, 205))


def make_dot():
    color = random.choice(color_list)
    timmy.pendown()
    timmy.dot(20,color)
make_dot()

cols = 0
rows = 0

while rows < 10:
    
    for cols in range(10):
        make_dot()
        timmy.penup()
        timmy.setheading(0)
        timmy.forward(50)
        cols += 1
    timmy.setx(x)
    y += 50
    timmy.sety(y)
    rows += 1






screen.exitonclick()




