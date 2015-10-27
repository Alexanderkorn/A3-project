__author__ = 'alexander'
import tkinter as tk

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


#new window

import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()