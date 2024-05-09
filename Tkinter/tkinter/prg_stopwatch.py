from tkinter import *
from datetime import datetime

temp = 0
after_id = ''

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    fix_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label.config(text=str(fix_temp))
    temp += 1

def start_sw():
    btnStart.grid_forget()
    btnStop.grid(row=1, columnspan=2, sticky=EW)
    tick()

def stop_sw():
    btnStop.grid_forget()
    btnContinue.grid(row=1, column=0, sticky=EW)
    btnReset.grid(row=1, column=1, sticky=EW)
    root.after_cancel(after_id)

def continue_sw():
    btnContinue.grid_forget()
    btnReset.grid_forget()
    btnStop.grid(row=1, columnspan=2, sticky=EW)
    tick()

def reset_sw():
    global temp
    temp = 0
    label.config(text='00:00')
    btnContinue.grid_forget()
    btnReset.grid_forget()
    btnStart.grid(row=1, columnspan=2, sticky=EW)

def print_space(event):
    btnStop.grid_forget()
    btnContinue.grid(row=1, column=0, sticky=EW)
    btnReset.grid(row=1, column=1, sticky=EW)
    root.after_cancel(after_id)

root = Tk()
root.title('Секундомер')

label = Label(root, width=5, font=('Impact', 100), text='00:00', fg='brown')
label.grid(row=0, columnspan=2)

btnStart = Button(root, font=('Arial Black', 30), text='Запуск', fg='green', command=start_sw)
btnStop = Button(root, font=('Arial Black', 30), text='Остановить', fg='red', command=stop_sw)
btnContinue = Button(root, font=('Arial Black', 30), text='Далее', fg='green', command=continue_sw)
btnReset = Button(root, font=('Arial Black', 30), text='Сброс', fg='red', command=reset_sw)

btnStart.grid(row=1, columnspan=2, sticky=EW)

root.bind('<space>', print_space)

root.mainloop()
