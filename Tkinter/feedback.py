from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):

        self.frame_top = ttk.Frame(master)
        self.frame_top.pack()

        self.logo = PhotoImage(file='/Users/mmvp/Desktop/Tkinter/tkinter_lynda/twit_logo.gif')
        self.small_logo = self.logo.subsample(4, 4)
        ttk.Label(self.frame_top, image=self.small_logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.frame_top, text='Оставьте отзыв').grid(row=0, column=1)
        ttk.Label(self.frame_top, wraplength=300, text=("Вы видите перед собой форму обратной связи. "
                                                        "Оставьте свой отзыв - Ваше мнение важно для нас."))\
                                                        .grid(row=1, column=1)

        self.frame_bottom = ttk.Frame(master)
        self.frame_bottom.pack()

        ttk.Label(self.frame_bottom, text='Логин:').grid(row=0, column=0, padx=5, sticky=EW)
        ttk.Label(self.frame_bottom, text='Email:').grid(row=0, column=1, padx=5, sticky=EW)
        ttk.Label(self.frame_bottom, text='Комментарий:').grid(row=2, column=0, padx=5, sticky=EW)

        self.entry_login = ttk.Entry(self.frame_bottom, width=20)
        self.entry_email = ttk.Entry(self.frame_bottom, width=20)
        self.text_comment = Text(self.frame_bottom, width=55, height=10)

        self.entry_login.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.text_comment.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.frame_bottom, text='OK', command=self.okay).grid(row = 4, column = 0, padx = 5, pady = 5, sticky=E)
        ttk.Button(self.frame_bottom, text='Очистить', command=self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky=W)
        self.style = ttk.Style()
        self.style.theme_use('classic')
        self.style.configure('TButton', foreground='blue')


    def okay(self):
        print('Логин: {}'.format(self.entry_login.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Комментарий: {}'.format(self.text_comment.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title='Наша обратная связь', message='Ваш комментарий учтен!')

    def clear(self):
        self.entry_login.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comment.delete(1.0, 'end')

def main():

    root = Tk()
    root.title('Обратная связь')
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__":
    main()
