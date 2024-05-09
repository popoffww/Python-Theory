from tkinter import *

root = Tk()

# mainmenu = Menu(root)
# root.config(menu=mainmenu)
#
# filemenu = Menu(mainmenu, tearoff=0)
# filemenu.add_command(label="Открыть...")
# filemenu.add_command(label="Новый")
# filemenu.add_command(label="Сохранить...")
# filemenu.add_command(label="Выход")
#
# helpmenu = Menu(mainmenu, tearoff=0)
# helpmenu.add_command(label="Помощь")
# helpmenu.add_command(label="О программе")
#
# mainmenu.add_cascade(label="Файл", menu=filemenu)
# mainmenu.add_cascade(label="Справка", menu=helpmenu)

root.option_add('*tearOff', False)
menubar = Menu(root)
root.config(menu = menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)

menubar.add_cascade(menu = file, label = 'File')
menubar.add_cascade(menu = edit, label = 'Edit')
menubar.add_cascade(menu = help_, label = 'Help')

file.add_command(label = 'New', command = lambda: print('New File'))
file.add_separator()
file.add_command(label = 'Open...', command = lambda: print('Opening File...'))
file.add_command(label = 'Save', command = lambda: print('Saving File...'))

# main_menu = Menu(root)
# root.config(menu=main_menu)

# first_item = Menu(main_menu)

# main_menu.add_cascade(label='File', menu=first_item)

# first_item.add_command(label='New')
# first_item.add_command(label='Exit')

root.mainloop()
