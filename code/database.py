__author__ = 'MuscioCraft'

import csv

with open('database.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])