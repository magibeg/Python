#using turtle to draw things on the screen
import turtle
import random

turtle.color('green')

for steps in range(22):
    r = random.randint(1,100)
    turtle.forward(r)
    turtle.right(r)

turtle.forward(250)
turtle.color('red')

numberOfSides = 12
for steps in range(numberOfSides):
    turtle.forward(100)
    turtle.right(360/numberOfSides)
    for steps in range(numberOfSides):
        turtle.forward(50)
        turtle.right(360/numberOfSides)
