from tkinter import *
from tkinter import ttk

class Joke:

    def __init__(self, root):
        self.label = ttk.Label(root, text='Я меняюсь!')
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(root, text='Нажми', command=self.not_touch).grid(row=1, column=0)
        ttk.Button(text='Нажми', command=self.hands_off).grid(row=1, column=1)

    def not_touch(self):
        self.label.config(text='Не трожь!')
    def hands_off(self):
        self.label.config(text='Руки!')


def main():
    root = Tk()
    root.title('Недотрога')
    app = Joke(root)
    root.mainloop()

if __name__ == '__main__':
    main()
