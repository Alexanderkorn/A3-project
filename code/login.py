__author__ = 'alexander'

import csv
import sys
import xml
import xmltodict
from xml.dom.minidom import parse
from xml.dom import minidom
# imports van bestaande files
#import film
#import sort
#import TKinter_gui
#import api #File binnen de map code. deze blijft een fout melding geven.
#film.x=input("Zender is: ")
a=input("Zender is: ")

#CVS
naambedrijf=""#TKinter_gui.zenders_leveranciers # Word later nog gebruikt
naamfilm=input("Film naam:")
database='database.csv'

def check_login():
    code = int(input("uw code alstublieft"))
    f=open("Usernames.csv",'r')
    reader=csv.reader(f, delimiter=';')

    for i in reader:
        if int(i[1]) == int(code):
            print(i[0])
            print("Succes")
    f.close()

                            # lijn 3
def check_aanbieder_csv():  # csv
    try:
        r=open(database, 'r')
    except:
        sys.exit("Unable to open: database.csv")
    global naambedrijf
    global naamfilm
    reader=csv.reader(r, delimiter=';')

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
        if naambedrijf == "NPO3":
            print("hoi")
        elif naambedrijf == "RTL4":
            print("Doei")
        elif naambedrijf == "RTL7":
            print("Test")
        elif naambedrijf == "RTL8":
            print("Blaa")
        elif naambedrijf == "Canvas":
            print("Looo")
        else:
            print("Sorry geen geldig zender.")
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

keywords = {"aasdf", "aasdfs"}
csv.field_size_limit(sys.maxsize)
invalids = 0
valids = 0
for filename in ['database.csv']:
    # The with statement in Python makes sure that your file is properly closed
    # (automatically) when an error occurs. This is a common idiom.
    # In addition, CSV files should be opened only in 'rb' mode.
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter='|', quotechar='\\')
        for row in reader:
            try:
                print(row)[2]
                valids += 1
            # Don't use bare except clauses. It will catch
            # exceptions you don't want or intend to catch.
            except IndexError:
                invalids += 1
            # The filtering is done here.
            for field in row:
                if field in keywords:
                    print(row)
                    break
# Prefer the str.format() method over the old style string formatting.
print('parsed {0} records. ignored {1}'.format(valids, invalids))
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
        check_login()
        check_aanbieder_csv()
    except:
        pass
    finally:
        break
