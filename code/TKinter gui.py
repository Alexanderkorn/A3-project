import tkinter as tk
import database

window = tk.Tk()
window.withdraw()

class Gebruikersnaam(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.Naam_invoer()

    def Naam_invoer(self):
        self.naam_invoer_vak = tk.Tk()
        w = 400
        h = 650
        ws = self.naam_invoer_vak.winfo_screenwidth()
        hs = self.naam_invoer_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.naam_invoer_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.naam_invoer_vak.configure(background="orange")
        label_naam = tk.Label(self.naam_invoer_vak, text="Uw naam: ")
        label_naam.pack(padx=10, pady=10, side=tk.LEFT)
        naaminvoer = tk.Entry(self.naam_invoer_vak)
        naaminvoer.pack(padx=10, pady=10, side=tk.RIGHT)
        verder_button = tk.Button(self.naam_invoer_vak, text="verder", command=self.Achternaam_invoer)
        verder_button.pack(side=tk.BOTTOM)
        self.naam_invoer_vak.mainloop()
        return naaminvoer

    def Achteraam_invoer(self):
        self.achternaam_invoer_vak = tk.Tk()
        w = 400
        h = 650
        ws = self.achternaam_invoer_vak.winfo_screenwidth()
        hs = self.achternaam_invoer_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.achternaam_invoer_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.achternaam_invoer_vak.configure(background="orange")
        label_naam = tk.Label(self.achternaam_invoer_vak, text="Uw achternaam: ")
        label_naam.pack(padx=10, pady=10, side=tk.LEFT)
        achternaaminvoer = tk.Entry(self.achternaam_invoer_vak)
        achternaaminvoer.pack(padx=10, pady=10, side=tk.RIGHT)
        verder_button = tk.Button(self.achternaam_invoer_vak, text="verder", command=self.Email_invoer)
        verder_button.pack(side=tk.BOTTOM)
        self.achternaam_invoer_vak.mainloop()
        return achternaaminvoer


    def Email_invoer(self):
        self.naam_invoer_vak.destroy()
        self.email_invoer_vak = tk.Tk()
        w = 400
        h = 650
        ws = self.email_invoer_vak.winfo_screenwidth()
        hs = self.email_invoer_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.email_invoer_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.email_invoer_vak.configure(background="orange")
        label_emailadres = tk.Label(self.email_invoer_vak, text="Uw E-mailadres: ")
        label_emailadres.pack(side=tk.LEFT)
        emailadres_invoer = tk.Entry(self.email_invoer_vak)
        emailadres_invoer.pack(side=tk.RIGHT)
        verder_button = tk.Button(self.email_invoer_vak, text="verder", command=None)
        verder_button.pack(side=tk.BOTTOM)
        self.email_invoer_vak.mainloop()
        return emailadres_invoer


App = Gebruikersnaam(master=window)
App.mainloop()

