from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Для рисования')

canvas = Canvas(root, width=1280, height=720, bg='white')
canvas.pack()

def mouse_press(event):
    global prev
    prev = event
    
def paint(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width=5)
    prev = event

root.bind('<ButtonPress>', mouse_press)
root.bind('<B1-Motion>', paint)

root.mainloop()

