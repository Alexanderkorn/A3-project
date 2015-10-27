__author__ = 'alexander'

import csv

import xmltodict

#import api #File binnen de map code. deze blijft een fout melding geven.

#CVS
naambedrijf=input("Film naam: ") # Word later nog gebruikt
database='database.csv'

#XML   dit deel hangt af van database.py en TKinter_gui.py
document = "<filmsoptv datum=""><film><regisseur></regisseur></film></filmsoptv>"
#dom = xml.dom.minidom.parseString(document)

                            # lijn 3
def check_aanbieder_csv():  # csv
    r=open(database, 'r')
    reader=csv.reader(r, delimiter=';')
    naamfilm=input("Film naam:")
    for row in reader:
        if row[3] == naamfilm:
            print(row[3])
        else:
            print("Niks")
    r.close()
    return row

def check_aanbieder_xml():# xml

    r=open('data.xml', 'rt')
    xml_string = r.read()
    return xmltodict.parse(xml_string)

#xmldict = check_aanbieder_xml()
#print(xmldict['data.xml']['regisseur'])

while True:
    try:                         #Bron voor name en api.api http://stackoverflow.com/questions/3781851/run-a-python-script-from-another-python-script-passing-in-args
        #if __name__=='__main__': # call the api.py
        #    api.api              # exicute api.py def api
        #os.system("api.py 1")
        check_aanbieder_csv()
        print(check_aanbieder_csv())
    except:
        pass
    finally:
        break
