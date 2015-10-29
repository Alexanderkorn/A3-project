import tkinter as tk
import sys
import xmltodict
import xml.dom.minidom
from xml.dom.minidom import parse

window = tk.Tk()
window.withdraw()

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
             writer = csv.writer(csvfile, delimiter=';', dialect='excel', lineterminator='\n')
             writer.writerow([App.naam, App.achternaam, App.emailadres, str(ticket)])

    except:
        sys.exit("Er is wat mis gegaan met het openen en of het schrijven van de database")


    try:
        print("Uw ticket nummer is : "+str(ticket))
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer printen.")

#bron: http://stackoverflow.com/questions/6653128/getting-text-between-xml-tags-with-minidom


def read():
    global zenders
    global zenders_en_films
    def read_xml():
        file = open('data.xml','r')
        xml_string = file.read()
        return xmltodict.parse(xml_string)

    film_nummer = None
    film_dict = read_xml()
    nodes = parse('data.xml')
    zenders=[]
    films=[]
    zenders_en_films = {}

    for film_nummer in nodes.getElementsByTagName('film'):

        document = film_nummer.toxml()
        dom = xml.dom.minidom.parseString(document)

        def getText(nodelist):
            rc = []
            for node in nodelist:
                if node.nodeType == node.TEXT_NODE:
                    rc.append(node.data)
            return ''.join(rc)

        def handleTok(tokenlist):
            texts = ""
            for token in tokenlist:
                texts += ""+ getText(token.childNodes)
            return texts
        foo = dom.getElementsByTagName("zender")
        text = handleTok(foo)
        b =text.split()
        zenders.extend(b)
        bob = dom.getElementsByTagName("titel")

        text2 = handleTok(bob)
        c =text2.split("\n")
        films.extend(c)
    for i in range(len(zenders)):
        if zenders[i] not in zenders_en_films:
            zenders_en_films[zenders[i]]=films[i]
        else:
            zenders_en_films[zenders[i]+' 2e film']=films[i]
        #print(text) # output zenders. read() is nodig om dit te laten werken

read()

LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 12)

class Gebruikersnaam(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.Selectie_scherm()

    def Selectie_scherm(self):
        self.selectie_scherm_vak = tk.Tk()
        w = 400
        h = 650
        ws = self.selectie_scherm_vak.winfo_screenwidth()
        hs = self.selectie_scherm_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.selectie_scherm_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.selectie_scherm_vak.configure(background="orange")
        label = tk.Label(self.selectie_scherm_vak, text="Bent u Leverancier of klant?", font="LARGE_FONT", background='orange')
        label.place(y=250, x=90)
        klant_button = tk.Button(self.selectie_scherm_vak, text="Klant", command=self.Naam_invoer)
        klant_button.place(y=300, x=140)
        leverancier_button = tk.Button(self.selectie_scherm_vak, text="Leverancier", command=self.Leveranciersnaam_invoer)
        leverancier_button.place(y=300, x=200)
        self.selectie_scherm_vak.mainloop()

    def Leveranciersnaam_invoer(self):
        global zenders
        self.selectie_scherm_vak.destroy()
        self.leverancier_invoer_vak = tk.Tk()
        w = 400
        h = 650
        ws = self.leverancier_invoer_vak.winfo_screenwidth()
        hs = self.leverancier_invoer_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.leverancier_invoer_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.leverancier_invoer_vak.configure(background="orange")
        label = tk.Label(self.leverancier_invoer_vak, text="Welke zender wordt laten zien?", font="LARGE_FONT", background='orange')
        label.place(y=150, x=65)
        leverancier_lijst = tk.Listbox(self.leverancier_invoer_vak)
        f = []

        for i in zenders:
            while i not in f:
                f.append(i)

        for i in f:
            leverancier_lijst.insert(tk.END, i)

        leverancier_lijst.place(y=200, x=135)
        quit_button = tk.Button(self.leverancier_invoer_vak, text="Afsluiten", font='NORMAL_FONT', command=self.Quit_button)
        quit_button.place(y=380, x=195)

        def nummer_leverancier():
            goede_nummer_leverancier = str(leverancier_lijst.curselection())
            index_goede_nummer_leverancier = int(goede_nummer_leverancier[1])
            global zender_leverancier
            zender_leverancier = zenders[index_goede_nummer_leverancier]
            self.Weergave_van_eigen_films()
        verder_button = tk.Button(self.leverancier_invoer_vak, text="Verder", command=(lambda: nummer_leverancier()))
        verder_button.place(y=380, x=140)
        self.leverancier_invoer_vak.mainloop()

    def Weergave_van_eigen_films(self):
        global zenders_en_films
        global zender_leverancier
        self.leverancier_invoer_vak.destroy()
        self.filmweergave_vak = tk.Tk()
        w = 400
        h = 650
        ws = self.filmweergave_vak.winfo_screenwidth()
        hs = self.filmweergave_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.filmweergave_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.filmweergave_vak.configure(background="orange")
        lijst_van_films = tk.Text(self.filmweergave_vak, background='orange')
        weergave_films_gekozen_zender_lijst = []
        weergave_films_gekozen_zender= ""
        for i in zenders_en_films:
            if i == zender_leverancier or i == zender_leverancier+' 2e film':
                weergave_films_gekozen_zender_lijst.append(zenders_en_films[i])
        for i in range(len(weergave_films_gekozen_zender_lijst)):
            print(weergave_films_gekozen_zender_lijst[i])
            weergave_films_gekozen_zender += weergave_films_gekozen_zender_lijst[i] + '\n'
        lijst_van_films.insert(tk.INSERT, weergave_films_gekozen_zender)
        lijst_van_films.place(height=100, width=250, y=240, x=75)
        label = tk.Label(self.filmweergave_vak, text="Deze films zijn op de zender "+zender_leverancier+':', font="LARGE_FONT", background='orange')
        label.place(y=175, x=50)
        verder_button = tk.Button(self.filmweergave_vak, text="Verder", command=(lambda: None))
        verder_button.place(y=380, x=140)
        quit_button = tk.Button(self.filmweergave_vak, text="Afsluiten", command=self.Quit_button)
        quit_button.place(y=380, x=195)
        self.filmweergave_vak.mainloop()

    def Naam_invoer(self):
        """Deze functie laat de gebruiker zijn/haar naam invoeren.
        """
        self.selectie_scherm_vak.destroy()
        self.voornaam_invoer_vak = tk.Tk()
        w = 400
        h = 650
        ws = self.voornaam_invoer_vak.winfo_screenwidth()
        hs = self.voornaam_invoer_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.voornaam_invoer_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.voornaam_invoer_vak.configure(background="orange")
        label = tk.Label(self.voornaam_invoer_vak, text="Gegevens invoeren", font="LARGE_FONT", background='orange')
        label.place(y=230, x=105)
        label_naam = tk.Label(self.voornaam_invoer_vak, text="Uw naam: ", background="orange")
        label_naam.place(y=300, x=100)
        naam_invoer = tk.Entry(self.voornaam_invoer_vak)
        naam_invoer.bind('<Return>', lambda event: self.Achternaam_invoer(naam_invoer.get()))
        naam_invoer.place(y=300, x=160)
        verder_button = tk.Button(self.voornaam_invoer_vak, text="Verder", command=(lambda: self.Achternaam_invoer(naam_invoer.get())))
        verder_button.place(y=350, x=140)
        quit_button = tk.Button(self.voornaam_invoer_vak, text="Afsluiten", command=self.Quit_button)
        quit_button.place(y=350, x=195)
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
        label = tk.Label(self.achternaam_invoer_vak, text="Gegevens invoeren", font="LARGE_FONT", background='orange')
        label.place(y=230, x=105)
        label_naam = tk.Label(self.achternaam_invoer_vak, text="Uw achternaam: ", background="orange")
        label_naam.place(y=300, x=65)
        achternaam_invoer = tk.Entry(self.achternaam_invoer_vak)
        achternaam_invoer.bind('<Return>', lambda event: self.Email_invoer(achternaam_invoer.get()))
        achternaam_invoer.place(y=300, x=160)
        verder_button = tk.Button(self.achternaam_invoer_vak, text="Verder", command=(lambda: self.Email_invoer(achternaam_invoer.get())))
        verder_button.place(y=350, x=140)
        quit_button = tk.Button(self.achternaam_invoer_vak, text="Afsluiten", command=self.Quit_button)
        quit_button.place(y=350, x=195)
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
        label = tk.Label(self.email_invoer_vak, text="Gegevens invoeren", font="LARGE_FONT", background='orange')
        label.place(y=230, x=105)
        label_emailadres = tk.Label(self.email_invoer_vak, text="Uw E-mailadres: ", background="orange")
        label_emailadres.place(y=300, x=65)
        self.emailadres_invoer = tk.Entry(self.email_invoer_vak)
        self.emailadres_invoer.bind('<Return>', lambda: self.Open_menu())
        self.emailadres_invoer.place(y=300, x=160)
        verder_button = tk.Button(self.email_invoer_vak, text="Verder", command=(lambda: self.Open_menu()))
        verder_button.place(y=350, x=140)
        quit_button = tk.Button(self.email_invoer_vak, text="Afsluiten", command=self.Quit_button)
        quit_button.place(y=350, x=195)
        self.email_invoer_vak.mainloop()
        return self.emailadres_invoer

    def Open_menu(self):
        self.Exit_program(self.emailadres_invoer.get())
        from navigation import ThuisBioscoop #kan beter maar hij opent bij importeren

    def Exit_program(self, emailadres):
        """Deze functie zorgt ervoor dat het programma compleet afgesloten wordt.
        """
        self.emailadres = emailadres
        self.email_invoer_vak.destroy()
        window.destroy()

    def Quit_button(self):
        """Deze functie zorgt ervoor dat het programma compleet afgesloten wordt.
        """
        sys.exit()

App = Gebruikersnaam(master=window)
App.mainloop()
ticket()

# ticket nummer in  window
