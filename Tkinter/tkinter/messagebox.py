from tkinter import *
from tkinter.messagebox import *
root = Tk()

buttonInfo = Button(root, text='Info', font=('Arial Black', 30),
command=lambda: showinfo('Show Info', 'Информация'))
buttonInfo.grid(row=0, column=0, sticky=EW)

buttonWarning = Button(root, text='Warning', font=('Arial Black', 30),
command=lambda: showwarning('Show Warning', 'Предупреждение'))
buttonWarning.grid(row=1, column=0, sticky=EW)

buttonError = Button(root, text='Error', font=('Arial Black', 30),
command=lambda: showerror('Show Error', 'Ошибка'))
buttonError.grid(row=2, column=0, sticky=EW)

root.mainloop()
