__author__ = 'Erwin'
import tkinter as tk
def datum_naar_film():
    """
    Vraag naar de datum en kijk of deze datum valid is.
    Aan de parameter dag geeft je de datum mee geschreven als: 26-10-2015. Je kunt alleen een request doen naar de TV-films voor vandaag en morgen.
    http://stackoverflow.com/questions/10002587/validating-date-both-format-and-value
    """
    import time
    import datetime
    global datum



    datum = input('Van welke dag wil je een film kijken? (dd-mm-yyyy) Alleen de datums van vandaag en morgen zijn geldig: ')
    try:
        valid_date = time.strptime(datum, '%d-%m-%Y')
        today_date=str(datetime.date.today().strftime('%d-%m-%Y'))
        tomorrow =  datetime.date.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%d-%m-%Y')
        if datum == today_date or datum == tomorrow:
            api()
        else:
            print ("Voer een geldige datum in.(Datum van vandaag of morgen) ")
    except ValueError:
        print('Invalid date!')
        datum_naar_film()




def api():
    """
    Benodigde modules: requests
    Aan de parameter apikey geeft je de eigen unieke API sleutel mee.
    Aan de parameter sorteer geeft je mee welke films je wilt ophalen. Dit is het getal 0, 1 of 2. Waar 0 staat voor: alle films, 1 staat voor: filmtips, 2 staat voor: 'film van de dag'.
    """
    import requests

    list = ['0', '1', '2']
    sorteren = input("Typ 0 voor Alle films \n1 voor filmtips \n2 voor film van de dag: ")

    while sorteren not in list:
        sorteren = input("Typ 0 voor Alle films \n1 voor filmtips \n2 voor film van de dag: ")

    request_filmtotaal = ('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=elqzcftw5jip13ijtki2z8mz74i14i6d&dag=%s&sorteer=%s' %(datum, sorteren))


    response = requests.get(request_filmtotaal)
    if response.text != "error:":
        with open('data.xml', 'w') as f:
            f.write(response.text)
    else:
        print("Er is een fout opgetreden")




def datum_invoer(self):
         """
    Vraag naar de datum en kijk of deze datum valid is.
    Aan de parameter dag geeft je de datum mee geschreven als: 26-10-2015. Je kunt alleen een request doen naar de TV-films voor vandaag en morgen.
    http://stackoverflow.com/questions/10002587/validating-date-both-format-and-value
    """
    self.selectie_scherm_vak.destroy()
        self.datum_invoer_vak = tk.Tk()
        w = 400
        h = 650
        ws = self.datum_invoer_vak.winfo_screenwidth()
        hs = self.datum_invoer_vak.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.datum_invoer_vak.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.datum_invoer_vak.configure(background="orange")
        label = tk.Label(self.voornaam_invoer_vak, text="Gegevens invoeren", font="LARGE_FONT", background='orange')
        label.place(y=230, x=105)
        label_naam = tk.Label(self.voornaam_invoer_vak, text="Uw naam: ", background="orange")
        label_naam.place(y=300, x=100)
        datum_invoer = tk.Entry(self.voornaam_invoer_vak)
        datum_invoer.bind('<Return>', lambda: self.Achternaam_invoer(datum_invoer.get()))
        datum_invoer.place(y=300, x=160)
        verder_button = tk.Button(self.voornaam_invoer_vak, text="Verder", command=(lambda: self.Achternaam_invoer(datum_invoer.get())), font=('Verdana', 10, 'bold'))
        verder_button.place(y=350, x=130)
        quit_button = tk.Button(self.voornaam_invoer_vak, text="Afsluiten", command=self.Quit_button, font=('Verdana', 10, 'bold'))
        quit_button.place(y=350, x=195)
        self.voornaam_invoer_vak.mainloop()
        return datum_invoer
datum_invoer()
