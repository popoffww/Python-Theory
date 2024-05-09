from tkinter import *

def left_click(event):
    frame1.config(bg='blue')
    frame2.config(bg='white')
    frame3.config(bg='white')

def right_click(event):
    frame1.config(bg='white')
    frame2.config(bg='white')
    frame3.config(bg='blue')

def middle_click(event):
    frame1.config(bg='white')
    frame2.config(bg='blue')
    frame3.config(bg='white')


root = Tk()
root.config(bg='black')

frame1 = Frame(width=250, height=250, bg='white')
frame2 = Frame(width=250, height=250, bg='white')
frame3 = Frame(width=250, height=250, bg='white')

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1, padx=1)
frame3.grid(row=0, column=2)

root.bind('<Button-1>', left_click)
root.bind('<Button-2>', right_click)
root.bind('<Button-3>', middle_click)

root.mainloop()