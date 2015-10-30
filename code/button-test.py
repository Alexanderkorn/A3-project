__author__ = 'Giuliano'



import tkinter as tk

gifdir = "./"
window = tk.Tk()
win = tk.Frame()


igm = tk.PhotoImage(file=gifdir+"poster.jpg")
tk.Button(win, image=igm).pack()
window.mainloop()

