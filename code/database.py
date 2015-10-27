__author__ = 'MuscioCraft'
import sys

def ticket():

    try:
        import csv
        from random import randint
    except:
        sys.exit("Er is wat fout gegaan met importeren van de functies.")


    try:
        ticket = randint(0,999999999)
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer aanmaken.")


    try:
        with open('database.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow([str(input("Uw naam :")).lower(), str(input("Uw E-mail adres :")).lower(), str(input("Welke film ? : (Moet nog een film selcteer menu in(andere opdracht))")).lower() , str(ticket)])
    except:
        sys.exit("Er is wat mis gegaan met het openen en of het scrijven van de database")


    try:
        print("Uw ticket nummer is : "+str(ticket))
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer printen.")


ticket()
