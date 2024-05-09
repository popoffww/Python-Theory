from tkinter import *

root = Tk()

label_1 = Label(root, text='Логин')
label_2 = Label(root, text='Пароль')

entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, column=0, sticky=E)
label_2.grid(row=1, column=0)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

button = Button(root, text='Войти')
button.grid(columnspan=2)

check = Checkbutton(root, text='Оставаться в системе')
check.grid(columnspan=2)




root.mainloop()