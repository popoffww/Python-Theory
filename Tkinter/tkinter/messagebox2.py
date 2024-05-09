from tkinter import *
from tkinter.messagebox import *
root = Tk()

def ask_question(event):
    answer = askquestion('Задать вопрос', 'Вопрос № 1')
    label1.config(text=answer)

def ask_ok(event):
    answer = askokcancel('Задать вопрос', 'Вопрос № 2')
    label2.config(text=answer)

def ask_yn(event):
    answer = askyesno('Задать вопрос', 'Вопрос № 3')
    label3.config(text=answer)

def ask_rc(event):
    answer = askretrycancel('Задать вопрос', 'Вопрос № 4')
    label4.config(text=answer)


button1 = Button(root, text='Задать вопрос', font=('Helvetica', 20), width=12)
button1.grid(row=0, column=0, sticky=EW)

label1 = Label(root, font=('Helvetica', 20), width=12)
label1.grid(row=0, column=1)

button1.bind('<Button-1>', ask_question)

button2 = Button(root, text='Отменить/ОК', font=('Helvetica', 20), width=12)
button2.grid(row=1, column=0, sticky=EW)

label2 = Label(root, font=('Helvetica', 20), width=12)
label2.grid(row=1, column=1)

button2.bind('<Button-1>', ask_ok)

button3 = Button(root, text='Да/Нет', font=('Helvetica', 20), width=12)
button3.grid(row=2, column=0, sticky=EW)

label3 = Label(root, font=('Helvetica', 20), width=12)
label3.grid(row=2, column=1)

button3.bind('<Button-1>', ask_yn)

button4 = Button(root, text='Retry/Cancel', font=('Helvetica', 20), width=12)
button4.grid(row=3, column=0, sticky=EW)

label4 = Label(root, font=('Helvetica', 20), width=12)
label4.grid(row=3, column=1)

button4.bind('<Button-1>', ask_rc)

root.mainloop()
