__author__ = 'alexander'

import csv

naambedrijf=input("uw bedrijfs naam:")
database='database.csv'
# lijn 3
def check_aanbieder():
    r=open(database, 'r')
    reader=csv.reader(r, delimiter=';')
    with open(database, 'r'):
        for row in reader:
            if naambedrijf == row[3]: # if the username shall be on column 3 (-> index 2)
                print("is in file")