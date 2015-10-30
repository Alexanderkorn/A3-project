import tkinter as tk
import sys
import xml.dom.minidom
from xml.dom.minidom import parse
from random import randint
import csv


window = tk.Tk()
window.withdraw()

def ticket(naam, achternaam, emailadres, film):

    try:
        #Er wordt een ticket nummer aangemaakt

        ticket = randint(0,999999999)
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer aanmaken.")


    try:
        #input in variabelen zetten(In in kleine letters)
        a=str(naam).lower()
        b=str(achternaam).lower()
        c=str(emailadres).lower()
        #read_xml() functie gebruiken, en tag3 als input. De 0 houd in dat text1 wordt gereturnd
        d=read_xml("titel","starttijd", film, 0)
        #read_xml() functie gebruiken en tag3 als input d. De 1 houd in dat text2 wordt gereturnd
        e=read_xml("titel","starttijd",d , 1)

        #database.csv wordt geopend en de data wordt weg geschreven.
        with open('database.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', dialect='excel', lineterminator='\n')
            writer.writerow([a,b,c,d,e,str(ticket).lower()])

    except:
        sys.exit("Er is wat mis gegaan met het openen en of het schrijven van de database")


    try:
        #ticket nummer wordt terug gegeven.
        print("Uw ticket nummer is : "+str(ticket))
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer printen.")

def read_xml(tag1, tag2="", tag3=None, tag4=None, tag5='film'):

    try:
        global zenders
        global zenders_en_films



        nodes = parse('data.xml')
        zenders=[]
        films=[]
        zenders_en_films = {}

            #tag3(standaard 'film') zijn de tags die uit 'data.xml' worden gehaalt
        for film_nummer in nodes.getElementsByTagName(tag5):

            #magie
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

            document = film_nummer.toxml()
            dom = xml.dom.minidom.parseString(document)

            #De text tussen tag 1 wordt in text1 gezet
            text1 = handleTok(dom.getElementsByTagName(tag1))
            #De text tussen tag 2 wordt in text2 gezet
            text2 = handleTok(dom.getElementsByTagName(tag2))
            if tag3 in text1:
                #Als tag 4 0 is dan wordt text1 gereturnd
                if tag4 == 0:
                    return text1
                #Als tag 4 1 is dan wordt text2 gereturnd
                elif tag4 == 1:
                    return text2
                else:
                   pass
            else:
                pass

            if tag4 == "1":
                foo = dom.getElementsByTagName("zender")
                text = handleTok(foo)
                b =text.split()
                zenders.extend(b)
                bob = dom.getElementsByTagName("titel")

                text2 = handleTok(bob)
                c =text2.split("\n")
                films.extend(c)
        if tag4 == "1":
            for i in range(len(zenders)):
                if zenders[i] not in zenders_en_films:
                    zenders_en_films[zenders[i]]=films[i]
                else:
                    zenders_en_films[zenders[i]+' 2e film']=films[i]
                #print(text) # output zenders. read() is nodig om dit te laten werken
    except:
        exit("Read_xml didn't work")

read_xml("","" , "" ,"1")

LARGE_FONT = ("Verdana", 12)
# NORMAL_FONT = (tk.font('Verdana', 12, 'bold'))

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
        label.place(y=250, x=80)
        klant_button = tk.Button(self.selectie_scherm_vak, text="Klant", command=self.Naam_invoer, font=('Verdana', 10, 'bold'))
        klant_button.place(y=300, x=120)
        leverancier_button = tk.Button(self.selectie_scherm_vak, text="Leverancier", command=self.Leveranciersnaam_invoer, font=('Verdana', 10, 'bold'))
        leverancier_button.place(y=300, x=190)
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
        def nummer_leverancier():
            goede_nummer_leverancier = str(leverancier_lijst.curselection())
            index_goede_nummer_leverancier = int(goede_nummer_leverancier[1])
            global zender_leverancier
            zender_leverancier = zenders[index_goede_nummer_leverancier]
            self.Weergave_van_eigen_films()
        verder_button = tk.Button(self.leverancier_invoer_vak, text="Verder", command=(lambda: nummer_leverancier()), font=('Verdana', 10, 'bold'))
        verder_button.place(y=380, x=130)
        quit_button = tk.Button(self.leverancier_invoer_vak, text="Afsluiten", command=self.Quit_button, font=('Verdana', 10, 'bold'))
        quit_button.place(y=420, x=160)
        terug_button = tk.Button(self.leverancier_invoer_vak, text="Terug", command=self.Selectie_scherm, font=('Verdana', 10, 'bold'))
        terug_button.place(y=380, x=195)
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
        lijst_van_films = tk.Text(self.filmweergave_vak, background='orange', font=('Verdana', 10))
        weergave_films_gekozen_zender_lijst = []
        weergave_films_gekozen_zender= ""
        for i in zenders_en_films:
            if i == zender_leverancier or i == zender_leverancier+' 2e film':
                weergave_films_gekozen_zender_lijst.append(zenders_en_films[i])
        for i in range(len(weergave_films_gekozen_zender_lijst)):
            weergave_films_gekozen_zender += weergave_films_gekozen_zender_lijst[i] + '\n'
        lijst_van_films.insert(tk.INSERT, weergave_films_gekozen_zender)
        lijst_van_films.place(height=100, width=250, y=240, x=75)
        label = tk.Label(self.filmweergave_vak, text="Deze films zijn op de zender "+zender_leverancier+':', font="LARGE_FONT", background='orange')
        label.place(y=175, x=50)
        verder_button = tk.Button(self.filmweergave_vak, text="Verder", command=(lambda: None), font=('Verdana', 10, 'bold'))
        verder_button.place(y=380, x=130)
        quit_button = tk.Button(self.filmweergave_vak, text="Afsluiten", command=self.Quit_button, font=('Verdana', 10, 'bold'))
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
        label_naam = tk.Label(self.voornaam_invoer_vak, text="Uw naam: ", background="orange", font=('Verdana', 10))
        label_naam.place(y=300, x=100)
        naam_invoer = tk.Entry(self.voornaam_invoer_vak)
        naam_invoer.bind('<Return>', lambda event: self.Achternaam_invoer(naam_invoer.get()))
        naam_invoer.place(y=300, x=170)
        verder_button = tk.Button(self.voornaam_invoer_vak, text="Verder", command=(lambda: self.Achternaam_invoer(naam_invoer.get())), font=('Verdana', 10, 'bold'))
        verder_button.place(y=350, x=130)
        quit_button = tk.Button(self.voornaam_invoer_vak, text="Afsluiten", command=self.Quit_button, font=('Verdana', 10, 'bold'))
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
        label_naam = tk.Label(self.achternaam_invoer_vak, text="Uw achternaam: ", background="orange", font=('Verdana', 10))
        label_naam.place(y=300, x=65)
        achternaam_invoer = tk.Entry(self.achternaam_invoer_vak)
        achternaam_invoer.bind('<Return>', lambda event: self.Email_invoer(achternaam_invoer.get()))
        achternaam_invoer.place(y=300, x=180)
        verder_button = tk.Button(self.achternaam_invoer_vak, text="Verder", command=(lambda: self.Email_invoer(achternaam_invoer.get())), font=('Verdana', 10, 'bold'))
        verder_button.place(y=350, x=130)
        quit_button = tk.Button(self.achternaam_invoer_vak, text="Afsluiten", command=self.Quit_button, font=('Verdana', 10, 'bold'))
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
        label_emailadres = tk.Label(self.email_invoer_vak, text="Uw E-mailadres: ", background="orange", font=('Verdana', 10))
        label_emailadres.place(y=300, x=55)
        self.emailadres_invoer = tk.Entry(self.email_invoer_vak)
        self.emailadres_invoer.bind('<Return>', lambda: self.Open_menu())
        self.emailadres_invoer.place(y=300, x=170)
        verder_button = tk.Button(self.email_invoer_vak, text="Verder", command=(lambda: self.Open_menu()), font=('Verdana', 10, 'bold'))
        verder_button.place(y=350, x=130)
        quit_button = tk.Button(self.email_invoer_vak, text="Afsluiten", command=self.Quit_button, font=('Verdana', 10, 'bold'))
        quit_button.place(y=350, x=195)
        self.email_invoer_vak.mainloop()
        return self.emailadres_invoer

    def Open_menu(self):
        self.Exit_program(self.emailadres_invoer.get())
        ticket(self.naam, self.achternaam, self.emailadres)
        #from navigation import ThuisBioscoop #kan beter maar hij opent bij importeren

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


# ticket nummer in  window
