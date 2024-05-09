from tkinter import  *

def print_char(event):
    label.config(text=event.char)

def print_su(event):
    label.config(text='Shift Up')

def print_cd(event):
    label.config(text='Ctrl Shift Down')

root = Tk()

label = Label(root, width=12, font=('Georgia', 100))
label.pack()

for i in range(65, 123):
    root.bind(chr(i), print_char)

root.bind('<Shift-Up>', print_su)
root.bind('<Control-Shift-Down>', print_cd)

root.mainloop()
