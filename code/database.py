__author__ = 'MuscioCraft'
import sys

def ticket():
    """

    Eerst import de functie de benodigde libraries.
    Dan wordt er een ticket nummer aangemaakt

    """
    try:
        import csv
        from random import randint
    except:
        sys.exit("Er is wat fout gegaan met importeren van de benodigde libraries.")



    try:
        ticket = randint(0,999999999)
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer aanmaken.")


    try:
        with open('database.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', dialect='excel', lineterminator='\n')
            writer.writerow([str(input("Uw voornaam :")).lower(), str(input("Uw achtenaam :")).lower(), str(input("Uw E-mail adres :")).lower(),str(input("Welke film ? : (Moet nog een film selcteer menu in(andere opdracht))")).lower() , str(ticket).lower()])

    except:
        sys.exit("Er is wat mis gegaan met het openen en of het schrijven van de database")


    try:
        print("Uw ticket nummer is : "+str(ticket))
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer printen.")

ticket()
