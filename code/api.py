__author__ = 'Erwin'
def api():
    """
    Benodigde modules: xmltodict en requests
    Aan de parameter apikey geeft je de eigen unieke API sleutel mee.
    Aan de parameter dag geeft je de datum mee geschreven als: 26-10-2015. Je kunt alleen een request doen naar de TV-films voor vandaag en morgen.
    Aan de parameter sorteer geeft je mee welke films je wilt ophalen. Dit is het getal 0, 1 of 2. Waar 0 staat voor: alle films, 1 staat voor: filmtips, 2 staat voor: 'film van de dag'.

    """
    import requests
    import xmltodict

    dag = input("welke dag?")
    sorteren = input("0, 1, 2")
    request_filmtotaal = ('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=elqzcftw5jip13ijtki2z8mz74i14i6d&dag=%s&sorteer=%s' %(dag, sorteren))


    response = requests.get(request_filmtotaal)

    print(response.text)
api()