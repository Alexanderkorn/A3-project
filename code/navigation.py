__author__ = 'Giuliano'

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class ThuisBioscoop(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="popcorn.ico")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print(param)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        # poster1 = tk.PhotoImage(file="poster.gif")

        button1 = ttk.Button(self, text="The Martian",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Kill Bill 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Star Wars: Episode IV",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()

        button4 = ttk.Button(self, text="Limitless",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()

        button5 = ttk.Button(self, text="007: Spectre",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()

        button6 = ttk.Button(self, text="Back to the future",
                            command=lambda: controller.show_frame(PageSix))
        button6.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The Martian", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kill Bill 2", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Star wars: Episode IV", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Limitless", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="007: Spectre", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Back to the future", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

app = ThuisBioscoop()
app.mainloop()