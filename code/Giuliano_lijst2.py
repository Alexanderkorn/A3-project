__author__ = 'Stijn'
__author__ = 'Stijn'
import tkinter as tk
from tkinter import ttk

class ThuisBioscoop(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        igm = tk.PhotoImage(file="./poster.jpg")

        button1 = ttk.Button(self, text="The Martian", image=igm,
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The Martian", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        def nummer_leverancier():
            goede_nummer_leverancier = str(leverancier_lijst.curselection())
            index_goede_nummer_leverancier = int(goede_nummer_leverancier[1])+1
            print(index_goede_nummer_leverancier)
            # aan het eind van de functie gaat hij door naar het nieuwe scherm -->
            #controller.show_frame(PageTwo)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="verder",
                            command=lambda: nummer_leverancier())
        button2.pack()

        leverancier_lijst = tk.Listbox(self)
        f = ["Piet", "Jan", "Hendrik", "Hugo"]

        for i in f:
            leverancier_lijst.insert(tk.END, i)
        # je hebt een button nodig in het scherm
        # de button voort de functie hierboven uit

        leverancier_lijst.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kill Bill 2", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame(Verify2))
        button2.pack()

# dkjldsjlkfs


app = ThuisBioscoop()
app.mainloop()