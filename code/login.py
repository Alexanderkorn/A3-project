__author__ = 'alexander'

import csv

database='database.csv'

def check_aanbieder():
    r=open(database, 'r')
    reader=csv.reader(r, delimiter=';')