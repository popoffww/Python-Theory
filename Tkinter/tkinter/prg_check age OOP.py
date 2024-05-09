from tkinter import *

class Question:
    def __init__(self, root):

        self.entry = Entry(root, width=3, font=15)
        self.button = Button(root, text='Проверить')
        self.label = Label(root, width=25, font=15)

        self.entry.grid(row=0, columnspan=2)
        self.button.grid(row=1, columnspan=2)
        self.label.grid(row=2, columnspan=2)

        self.button.bind('<Button-1>', self.answer)

    def answer(self, event):
        txt = self.entry.get()

        try:
            if int(txt) < 18:
                self.label['text'] = 'Продажа алкоголя с 18 лет'
            else:
                self.label['text'] = 'Добро пожаловать!'
        except:
            self.label['text'] = 'Введите числовое значение'


root = Tk()
root.title('Введите Ваш возраст')

q = Question(root)

root.mainloop()
