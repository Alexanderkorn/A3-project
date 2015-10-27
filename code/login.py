__author__ = 'alexander'

import csv

import xmltodict


naambedrijf=input("uw bedrijfs naam:")
database='database.csv'
# lijn 3
def check_aanbieder_csv():# csv
    r=open(database, 'r')
    reader=csv.reader(r, delimiter=';')
    global naambedrijf
    for i in reader:
        if naambedrijf == i: # if the username shall be on column 3 (-> index 2)
            print("is in file")
        else:
            print("Niet in bestand")
    r.close()
    return i()
print(check_aanbieder_csv())

def check_aanbieder_xml():# xml
    r=open('data.xml', 'r')
    xml_string = r.read()
    return xmltodict.parse(xml_string)

xmldict = check_aanbieder_xml()
#print(xmldict['data.xml']['regisseur'])