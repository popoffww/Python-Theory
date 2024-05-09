from tkinter import *
from tkinter import ttk

def not_touch(event):
    label.config(text='Не трожь!')
def hands_off(event):
    label.config(text='Руки!')

window = Tk()
window.title('Недотрога')
# window.resizable(True, True)
# window.maxsize(640, 480)
# window.minsize(200, 200)
# window.geometry('640x480+50+100')
panedwindow = ttk.Panedwindow(window)
frame1 = ttk.Frame(panedwindow, width = 100, height = 600, relief = SUNKEN)
panedwindow.pack(fill = BOTH, expand = True)



label = ttk.Label(panedwindow, text='Я меняюсь!')
label.grid(row=0, column=0, columnspan=2)

button1 = ttk.Button(panedwindow, text='Нажми')
button2 = ttk.Button(panedwindow, text='Нажми')
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)

checkbutton = ttk.Checkbutton(panedwindow, text='Spam?')
checkbutton.grid(row=3, column=0)
radiobutton = ttk.Radiobutton(panedwindow, text='Eggs?')
radiobutton.grid(row=3, column=1)

button1.bind('<Button-1>', not_touch)
button2.bind('<Button-1>', hands_off)

window.mainloop()
