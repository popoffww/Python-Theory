from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.geometry('500x500')

def change_place(event):
    button.place(relx=random.random())
    button.place(rely=random.random())

logo = PhotoImage(file='/Users/mmvp/Desktop/Tkinter/python_logo.gif')
small_logo = logo.subsample(3,3)
button = ttk.Button(image=small_logo)
button.place(relx=0.5, rely=0.5, anchor='center')

root.bind('<1>', change_place)
root.bind('<space>', change_place)

root.mainloop()
