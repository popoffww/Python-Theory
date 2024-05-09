from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text='Кнопка1', fg='red')
button2 = Button(top_frame, text='Кнопка2', fg='green')
button3 = Button(top_frame, text='Кнопка3', fg='blue')
button4 = Button(bottom_frame, text='Кнопка4', fg='brown')
button5 = Button(bottom_frame, text='Кнопка5', fg='magenta')
button6 = Button(bottom_frame, text='Кнопка6', fg='purple')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(sid=LEFT)
button4.pack(side=RIGHT)
button5.pack(side=RIGHT)
button6.pack(side=RIGHT)


root.mainloop()