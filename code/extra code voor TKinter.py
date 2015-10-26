__author__ = 'alexander'
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("100x100")
root.configure(background='orange')

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.check_in_Widget()
        self.check_out_Widget()


    def check_in_Widget(self):
        self.check_in = tk.Button(self)
        self.check_in["text"] = "Check in"
        self.check_in["command"] = self.say_check_in
        self.check_in.pack(side="top")

    def check_out_Widget(self):
        self.check_out = tk.Button(self)
        self.check_out["text"] = "Check out"
        self.check_out["command"] = self.say_check_out
        self.check_out.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_check_in(self):
        root.configure(background="yellow")
        root.after(500, white)
        print("Ingechecked!")

    def say_check_out(self):
        root.configure(background="black")
        root.after(500, white)
        print("Uitgechecked!")

def white(*args,**kwargs):
    root.configure(background="orange")

app = Application(master=root)
app.mainloop()