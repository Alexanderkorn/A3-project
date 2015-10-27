__author__ = 'Giuliano'
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("400x650")
root.configure(background='orange')

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.check_in_Film1()
        self.check_in_Film2()
        self.check_in_Film3()
        self.check_in_Film4()
        self.check_in_Film5()
        self.check_in_Film6()

    def check_in_Film1(self):
        self.config(height=100, width=100)
        self.check_in = tk.Button(self)
        self.check_in["text"] = "The Martian"
        self.check_in["command"] = self.say_choice_film1
        self.check_in.pack(side="top")


    def check_in_Film2(self):
        self.check_in = tk.Button(self)
        self.check_in["text"] = "Star Wars"
        self.check_in["command"] = self.say_choice_film2
        self.check_in.pack(side="top")

    def check_in_Film3(self):
        self.check_in = tk.Button(self)
        self.check_in["text"] = "007: Spectre"
        self.check_in["command"] = self.say_choice_film3
        self.check_in.pack(side="top")

    def check_in_Film4(self):
        self.check_in = tk.Button(self)
        self.check_in["text"] = "Lord of the Rings: The Fellowship"
        self.check_in["command"] = self.say_choice_film4
        self.check_in.pack(side="top")

    def check_in_Film5(self):
        self.check_in = tk.Button(self)
        self.check_in["text"] = "Kill Bill 2"
        self.check_in["command"] = self.say_choice_film5
        self.check_in.pack(side="top")

    def check_in_Film6(self):
        self.check_in = tk.Button(self)
        self.check_in["text"] = "The Ring"
        self.check_in["command"] = self.say_choice_film6
        self.check_in.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")
        self.QUIT.place(x=0, y=0)

    def say_choice_film1(self):
        root.configure(background="yellow")
        root.after(white)
        print("U heeft gekozen voor The Martian")

    def say_choice_film2(self):
        root.configure(background="black")
        root.after(white)
        print("U heeft gekozen voor Star Wars")

    def say_choice_film3(self):
        root.configure(background="black")
        root.after(white)
        print("U heeft gekozen voor 007: Spectre")

    def say_choice_film4(self):
        root.configure(background="black")
        root.after(white)
        print("U heeft gekozen voor Lord of the Rings: The Fellowship")

    def say_choice_film5(self):
        root.configure(background="black")
        root.after(white)
        print("U heeft gekozen voor Kill Bill 2")

    def say_choice_film6(self):
        root.configure(background="black")
        root.after(white)
        print("U heeft gekozen voor The Ring")

def white(*args,**kwargs):
    root.configure(background="orange")

app = Application(master=root)
root.mainloop()
