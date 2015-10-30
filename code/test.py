__author__ = 'Roy', 'Mike'
import csv

def achternamen(row1, row2):
    #database.csv wordt geopend en in reader gezet
    try:
        f=open('database.csv','r')
        reader=csv.reader(f, delimiter=';')
    except:
        exit("'database.csv' kon niet geopend worden")

    #Row[row1] en row[row2] worden in een lijst gezet
    try:
        x=0
        list=[]
        for row in reader:

            if x == 0:
                x=1
                pass

            else:
                a = row[row1]
                b = row[row2]
                c = a , b
                list.append(c)

        print (sorted(list))
    except:
        exit("Lijst kon niet worden gemaakt")
    #f wordt gesloten
    try:
        f.close()
    except:
        print("Bestandt kon niet gesloten worden")

achternamen(4, 1)
achternamen(1, 4)