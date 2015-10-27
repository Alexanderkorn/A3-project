__author__ = 'alexander'

import csv

import xmltodict

import api

#CVS
naambedrijf=''#input("uw bedrijfs naam:")
database='database.csv'

#XML
document = "<filmsoptv datum=""><film><regisseur></regisseur></film></filmsoptv>"
#dom = xml.dom.minidom.parseString(document)

                            # lijn 3
def check_aanbieder_csv():  # csv
    r=open(database, 'r')
    reader=csv.reader(r, delimiter=';')
    naamfilm=input("uw bedrijfs naam:")
    for i in reader:
        if i[3] == naamfilm:
            print("is in file")
        else:
            print("Niet in bestand")
    print(naamfilm)
    return
    r.close()

def check_aanbieder_xml():# xml

    r=open('data.xml', 'rt')
    xml_string = r.read()
    return xmltodict.parse(xml_string)

#xmldict = check_aanbieder_xml()
#print(xmldict['data.xml']['regisseur'])

while True:
    try:                         #Bron voor name en api.api http://stackoverflow.com/questions/3781851/run-a-python-script-from-another-python-script-passing-in-args
        if __name__=='__main__': # call the api.py
            api.api              # exicute api.py def api
        #os.system("api.py 1")
        check_aanbieder_csv()
    except:
        pass
    finally:
        break
