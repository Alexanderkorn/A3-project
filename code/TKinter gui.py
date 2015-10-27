import tkinter as tk


window = tk.Tk()
window.withdraw()

class Gebruikersnaam(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.Naam_invoer()

    def Naam_invoer(self):
        self.voornaam_invoer_vak = tk.Tk()
        w = 400
        h = 650
        ws = self.voornaam_invoer_vak.winfo_screenwidth()
        hs = self.voornaam_invoer_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.voornaam_invoer_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.voornaam_invoer_vak.configure(background="orange")
        label_naam = tk.Label(self.voornaam_invoer_vak, text="Uw naam: ", background="orange")
        label_naam.pack(padx=10, pady=10, side=tk.LEFT)
        naam_invoer = tk.Entry(self.voornaam_invoer_vak)
        naam_invoer.pack(padx=10, pady=10, side=tk.RIGHT)
        verder_button = tk.Button(self.voornaam_invoer_vak, text="verder", command=self.Achternaam_invoer)
        verder_button.pack(side=tk.BOTTOM)
        self.voornaam_invoer_vak.mainloop()
        return naam_invoer

    def Achternaam_invoer(self):
        self.voornaam_invoer_vak.destroy()
        self.achternaam_invoer_vak = tk.Tk()
        w = 400
        h = 650
        ws = self.achternaam_invoer_vak.winfo_screenwidth()
        hs = self.achternaam_invoer_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.achternaam_invoer_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.achternaam_invoer_vak.configure(background="orange")
        label_naam = tk.Label(self.achternaam_invoer_vak, text="Uw achternaam: ", background="orange")
        label_naam.pack(padx=10, pady=10, side=tk.LEFT)
        achternaam_invoer = tk.Entry(self.achternaam_invoer_vak)
        achternaam_invoer.pack(padx=10, pady=10, side=tk.RIGHT)
        verder_button = tk.Button(self.achternaam_invoer_vak, text="verder", command=self.Email_invoer)
        verder_button.pack(side=tk.BOTTOM)
        self.achternaam_invoer_vak.mainloop()
        return achternaam_invoer


    def Email_invoer(self):
        self.achternaam_invoer_vak.destroy()
        self.email_invoer_vak = tk.Tk()
        w = 400
        h = 650
        ws = self.email_invoer_vak.winfo_screenwidth()
        hs = self.email_invoer_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.email_invoer_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.email_invoer_vak.configure(background="orange")
        label_emailadres = tk.Label(self.email_invoer_vak, text="Uw E-mailadres: ", background="orange")
        label_emailadres.pack(side=tk.LEFT)
        emailadres_invoer = tk.Entry(self.email_invoer_vak)
        emailadres_invoer.pack(side=tk.RIGHT)
        verder_button = tk.Button(self.email_invoer_vak, text="verder", command=None)
        verder_button.pack(side=tk.BOTTOM)
        self.email_invoer_vak.mainloop()
        return emailadres_invoer


App = Gebruikersnaam(master=window)
App.mainloop()

