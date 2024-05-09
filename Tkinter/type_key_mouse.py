from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Учим Tkinter')

def key_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('char: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}'.format(event.keycode))

root.bind('<KeyPress>', key_press)

canvas = Canvas(root, width=640, height=480, bg='white')
canvas.pack()

def mouse_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num))
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
    print('x_root: {}'.format(event.x_root))
    print('y_root: {}'.format(event.y_root))

root.bind('<ButtonPress>', mouse_press)

root.mainloop()

