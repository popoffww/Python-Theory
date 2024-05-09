
import turtle
import random

answer = ''
while answer!= 'n':
    answer = turtle.textinput('Рисуем окружность?','y : n')
    if answer == 'y':
        turtle.penup()
        turtle.goto(random.randrange(-300,300),random.randrange(-300,300))
        turtle.pendown()
        turtle.fillcolor(random.random(),random.random(),random.random())
        turtle.begin_fill()
        turtle.circle(random.randrange(1,100))
        turtle.end_fill()
    else:
        pass



