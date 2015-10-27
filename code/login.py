__author__ = 'alexander'

import csv

database='database.csv'
# lijn 3
def check_aanbieder():
    r=open(database, 'r')
    reader=csv.reader(r, delimiter=';')
