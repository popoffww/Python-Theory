from tkinter import *
from tkinter import ttk

class Feedback:

    def __init__(self, master):

        self.frame_top = ttk.Frame(master)
        self.frame_top.pack()

        self.logo = PhotoImage(file='/Volumes/MacData/Motion/pics/twit_logo.gif')
        self.small_logo = self.logo.subsample(3, 3)
        ttk.Label(self.frame_top, image=self.small_logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.frame_top, text='Lorem Ipsum').grid(row=0, column=1)
        ttk.Label(self.frame_top, wraplength=275, text=("Lorem Ipsum - это текст-'рыба', часто используемый в печати и вэб-дизайне. "
                                                        "Lorem Ipsum является стандартной 'рыбой' для текстов на латинице с начала XVI века.")).grid(row=1, column=1)



def main():

    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__":
    main()
