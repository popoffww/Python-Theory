from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Учим Tkinter')

def callback(call):
    print(call)
    
ttk.Button(root, text='Жми, не бойся 1', command=lambda:callback('Вызов 1')).pack()
ttk.Button(root, text='Жми, не бойся 2', command=lambda:callback('Вызов 2')).pack()
ttk.Button(root, text='Жми, не бойся 3', command=lambda:callback('Вызов 3')).pack()

def shortcut(action):
    print(action)

root.bind('<Control-c>', lambda e:shortcut('Копировать'))
root.bind('<Control-v>', lambda e:shortcut('Вставить'))



label1 = Label(root, text= 'Label 1')
label2 = Label(root, text= 'Label 2')
label1.pack()
label2.pack()

label1.bind('<ButtonPress>', lambda e: print('ButtonPress_Label'))
label1.bind('<1>', lambda e: print('1_Label'))
root.bind('<1>', lambda e: print('Root_Label'))
root.bind_all('<Escape>', lambda e: print('Escape'))

root.mainloop()
