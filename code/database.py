__author__ = 'MuscioCraft'

def ticket():


    import csv
    from random import randint
    ticket = randint(0,999999999)

    with open('database.csv', 'a') as csvfile:

        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([input("Uw naam :"), input("Uw E-mail adres :"), ticket])

    print("Uw ticket nummer is : "+ticket)

ticket()
