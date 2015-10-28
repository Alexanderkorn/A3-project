__author__ = 'alexander'

import csv
import sys
import xml
import xmltodict
from xml.dom.minidom import parse
from xml.dom import minidom
# imports van bestaande files
import film
import sort
#import api #File binnen de map code. deze blijft een fout melding geven.

#CVS
naambedrijf=input("Naam bedrijf: ") # Word later nog gebruikt
naamfilm='' #Word ook later gebruikt
naamzender=input("Naam van de zender: ")
database='database.csv'

def log_in():
    credentials = {}
    with open('Usernames.txt', 'r') as f:
        for line in f:
            user, pwd = line.strip().split(':')
            credentials[user] = pwd
            print(pwd)
            print(user)

                            # lijn 3
def check_aanbieder_csv():  # csv
    try:
        r=open(database, 'r')
    except:
        sys.exit("Unable to open: database.csv")
    global naambedrijf
    global naamfilm
    reader=csv.reader(r, delimiter=';')
    naamfilm=input("Film naam:")
    try:
        # if naambedrijf == "20fox":
        #     print("welkom "+naambedrijf)
        #     print("De film: ", naamfilm, " komt ", naamfilm.count(naamfilm), " voor in de database.")
        #     if naamfilm == "specter" or "house of carts":
        #         print(naamfilm.count(naamfilm))
        # elif naambedrijf == "lionsgate":
        #     print("welkom "+naambedrijf)
        #     print("De film: ", naamfilm, " komt ", naamfilm.count(naamfilm), " voor in de database.")
        #     if naamfilm == "specter" or "house of carts":
        #         print(naamfilm.count(naamfilm))
        if naambedrijf == "":
            print("hoi")
        else:
            print("Sorry geen geldig bedrijf.")
            pass
    except:
        print("Sorry geen geldig bedrijf.")

    for row in reader:
        if row[3] == naamfilm:
            print(row[3])
        else:
            return #print("Niks")
    try:
        r.close()
    except:
        sys.exit("Unable to close database.csv")
    return row
"""""
#XML   dit deel hangt af van database.py en TKinter_gui.py


document = "<filmsoptv><film>><zender></zender></film></filmsoptv>"
dom = xml.dom.minidom.parseString(document)
doc = minidom.parse('data.xml')

name = doc.getElementsByTagName("film")[0]
print(name.firstChild.data)

def check_aanbieder_xml():# xml
    r=open('data.xml', 'rt')
    xml_string = r.read()
    return xmltodict.parse(xml_string)

xmldict = check_aanbieder_xml()
print(xmldict[naamzender])

films = doc.getElementsByTagName("film")
for xml_reader_out in films:
        #sid = xml_reader_out.getAttribute("id")
        #nickname = xml_reader_out.getElementsByTagName("nickname")[0]
        zender = xml_reader_out.getElementsByTagName("zender")[0]
        print("zender:% " % (zender)) #id:%s, nickname:%s, salary:%s(zender))#.firstChild.data))

film_nummer = None
film_dict = check_aanbieder_xml()
nodes = parse('data.xml')
for film_nummer in nodes.getElementsByTagName('zender'): # 7 = in range of childnodes
    #print(film_dict['filmsoptv']['film'][film_nummer]['starttijd'])
    print(film_nummer.toxml())
"""""
while True:
    try:                         #Bron voor name en api.api http://stackoverflow.com/questions/3781851/run-a-python-script-from-another-python-script-passing-in-args
        #if __name__=='__main__': # call the api.py
        #    api.api              # exicute api.py def api
        #check_aanbieder_csv()
        log_in()
    except:
        pass
    finally:
        break
