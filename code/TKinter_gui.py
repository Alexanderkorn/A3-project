#from database import *
import tkinter as tk
import sys

def ticket():
    """

    Eerst import de functie de benodigde functies.
    Dan wordt er een ticket nummer aangemaakt

    """
    try:
        import csv
        from random import randint
    except:
        sys.exit("Er is wat fout gegaan met importeren van de functies.")



    try:
        ticket = randint(0,999999999)
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer aanmaken.")


    try:
        with open('database.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow([App.naam, App.achternaam, App.emailadres, str(ticket)])

    except:
        sys.exit("Er is wat mis gegaan met het openen en of het scrijven van de database")


    try:
        print("Uw ticket nummer is : "+str(ticket))
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer printen.")


window = tk.Tk()
window.withdraw()

class Gebruikersnaam(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.Naam_invoer()

    def Naam_invoer(self):
        """Deze functie laat de gebruiker zijn/haar naam invoeren.
        """
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
        label_naam.place(y=300, x=100)
        naam_invoer = tk.Entry(self.voornaam_invoer_vak)
        naam_invoer.place(y=300, x=160)
        verder_button = tk.Button(self.voornaam_invoer_vak, text="verder", command=(lambda: self.Achternaam_invoer(naam_invoer.get())))
        verder_button.place(y=350, x=200)
        quit_button = tk.Button(self.voornaam_invoer_vak, text="Afsluiten", command=self.Quit_button)
        quit_button.place(y=250, x=180)
        self.voornaam_invoer_vak.mainloop()
        return naam_invoer

    def Achternaam_invoer(self, naam):
        """Deze functie laat de gebruiker zijn/haar naam invoeren.
        """
        self.voornaam_invoer_vak.destroy()
        self.achternaam_invoer_vak = tk.Tk()
        self.naam = naam
        w = 400
        h = 650
        ws = self.achternaam_invoer_vak.winfo_screenwidth()
        hs = self.achternaam_invoer_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.achternaam_invoer_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.achternaam_invoer_vak.configure(background="orange")
        label_naam = tk.Label(self.achternaam_invoer_vak, text="Uw achternaam: ", background="orange")
        label_naam.pack(side=tk.LEFT)
        achternaam_invoer = tk.Entry(self.achternaam_invoer_vak)
        achternaam_invoer.pack(side=tk.RIGHT)
        verder_button = tk.Button(self.achternaam_invoer_vak, text="verder", command=(lambda: self.Email_invoer(achternaam_invoer.get())))
        verder_button.pack(side=tk.BOTTOM)
        self.achternaam_invoer_vak.mainloop()
        return achternaam_invoer

    def Email_invoer(self, achternaam):
        """Deze functie laat de gebruiker zijn/haar email invoeren.
        """
        self.achternaam = achternaam
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
        verder_button = tk.Button(self.email_invoer_vak, text="verder", command=(lambda: self.Exit_program(emailadres_invoer.get())))
        verder_button.pack(side=tk.BOTTOM)
        self.email_invoer_vak.mainloop()
        return emailadres_invoer

    def Exit_program(self, emailadres):
        """Deze functie zorgt ervoor dat het programma compleet afgesloten wordt.
        """
        self.emailadres = emailadres
        self.email_invoer_vak.destroy()
        window.destroy()

    def Quit_button(self):
        sys.exit()

App = Gebruikersnaam(master=window)

App.mainloop()

ticket()