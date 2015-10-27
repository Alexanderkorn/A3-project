__author__ = 'alexander'

import csv

import xmltodict


naambedrijf=input("uw bedrijfs naam:")
database='database.csv'
# lijn 3
def check_aanbieder_csv():# csv
    r=open(database, 'r')
    reader=csv.reader(r, delimiter=';')
    with open(database, 'r'):
        for row in reader:
            if naambedrijf == row[3]: # if the username shall be on column 3 (-> index 2)
                print("is in file")

def check_aanbieder_xml():# xml
    r=open('data.xml', 'r')
    xml_string = r.read()
    return xmltodict.parse(xml_string)

xmldict = check_aanbieder_xml()
print(xmldict['data.xml']['regisseur'])