from tkinter import *

root = Tk()

one = Label(root, text='Один', bg='red', fg='yellow')
two = Label(root, text='Два', bg='blue', fg='white')
three = Label(root, text='Три', bg='purple', fg='violet')

one.pack()
two.pack(fill=X)
three.pack(side=LEFT, fill=Y)



root.mainloop()
