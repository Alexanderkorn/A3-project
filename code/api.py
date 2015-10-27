__author__ = 'Erwin'

def datum_naar_film():
    """
    Vraag naar de datum en kijk of deze datum valid is.
    Aan de parameter dag geeft je de datum mee geschreven als: 26-10-2015. Je kunt alleen een request doen naar de TV-films voor vandaag en morgen.
    http://stackoverflow.com/questions/10002587/validating-date-both-format-and-value
    """
    import time
    import datetime
    global datum
    datum = input('Op welke datum wil je een film kijken? Je kan alleen kiezen voor vandaag of morgen (dd-mm-yyyy): ')
    try:
        valid_date = time.strptime(datum, '%d-%m-%Y')
        today_date=(datetime.date.today())
        tomorrow_date=datetime.date.today() + datetime.timedelta(days=1)
        if datum != today_date or tomorrow_date :
            print ("Alleen vandaag en morgen zijn geldige datums")
            datum_naar_film()
        else:
            print (" ")
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

    datum_naar_film()

    sorteren = input("Typ 0 voor Alle films \n1 voor filmtips \n2 voor film van de dag: ")

    request_filmtotaal = ('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=elqzcftw5jip13ijtki2z8mz74i14i6d&dag=%s&sorteer=%s' %(datum, sorteren))


    response = requests.get(request_filmtotaal)
    if response.text != "error:":
        with open('data.xml', 'w') as f:
            f.write(response.text)
    else:
        print("Er is een fout opgetreden")
#    print(response.text)
api()