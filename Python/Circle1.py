from turtle import *

speed(0)
bgcolor("Black")
colors = ['Red','White']
hideturtle()

for i in range(200):
    goto(0,0)
    color(colors[i%2])
    forward(i*2)
    left(3)
    circle(40)
    forward(130)
    right(180)

done()