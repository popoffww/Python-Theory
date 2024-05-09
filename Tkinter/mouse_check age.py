from tkinter import *

def output(event):
    txt = entry.get()

    try:
        if int(txt) < 18:
          label['text'] = 'Продажа алкоголя с 18 лет'
        else:
          label['text'] = 'Добро пожаловать!'
    except:
        label['text'] = 'Введите числовое значение'

root = Tk()
root.title('Введите Ваш возраст')

entry = Entry(root, width=3, font=15)
button = Button(root, text='Проверить')
label = Label(root, width=25, font=15)

entry.grid(row=0, columnspan=2)
button.grid(row=1,columnspan=2)
label.grid(row=2,columnspan=2)

button.bind('<Button-1>', output)

root.mainloop()
