__author__ = 'Giuliano'

gifdir = "./"
from tkinter import *
win = Tk()
igm = PhotoImage(file=gifdir+"poster.gif")
Button(win, image=igm).pack()
win.mainloop()

