# Прямоугольник
import turtle
def rectangle(width, height):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)

rectangle(400,300)