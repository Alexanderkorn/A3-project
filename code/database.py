__author__ = 'MuscioCraft'
import sys
#bron: http://stackoverflow.com/questions/6653128/getting-text-between-xml-tags-with-minidom

import xmltodict
import xml.dom.minidom
import csv
from xml.dom.minidom import parse

x = None
def test(x):

    def read_xml():
        file = open('data.xml','r')
        xml_string = file.read()
        return xmltodict.parse(xml_string)

    film_nummer = None
    film_dict = read_xml()
    nodes = parse('data.xml')

    for film_nummer in nodes.getElementsByTagName('film'):

        document = film_nummer.toxml()
        dom = xml.dom.minidom.parseString(document)

        def getText(nodelist):
            rc = []
            for node in nodelist:
                if node.nodeType == node.TEXT_NODE:
                    rc.append(node.data)
            return ''.join(rc)

        def handleTok(tokenlist):
            texts = ""
            for token in tokenlist:
                texts += ""+ getText(token.childNodes)
            return texts
        foo = dom.getElementsByTagName("titel")
        text = handleTok(foo)

        bob = dom.getElementsByTagName("starttijd")
        text2 = handleTok(bob)


        if x in text:
            return text
def test2(x):

    def read_xml():
        file = open('data.xml','r')
        xml_string = file.read()
        return xmltodict.parse(xml_string)

    film_nummer = None
    film_dict = read_xml()
    nodes = parse('data.xml')

    for film_nummer in nodes.getElementsByTagName('film'):

        document = film_nummer.toxml()
        dom = xml.dom.minidom.parseString(document)

        def getText(nodelist):
            rc = []
            for node in nodelist:
                if node.nodeType == node.TEXT_NODE:
                    rc.append(node.data)
            return ''.join(rc)

        def handleTok(tokenlist):
            texts = ""
            for token in tokenlist:
                texts += ""+ getText(token.childNodes)
            return texts
        foo = dom.getElementsByTagName("titel")
        text = handleTok(foo)

        bob = dom.getElementsByTagName("starttijd")
        text2 = handleTok(bob)

        if x in text:
            return text2





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
        a=str(input("Uw voornaam :")).lower()
        b=str(input("Uw achtenaam :")).lower()
        c=str(input("Uw E-mail adres :")).lower()
        d=test(str(input("Welke film ? : ")))
        e=test2(d)



        with open('database.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', dialect='excel', lineterminator='\n')
            writer.writerow([a,b,c,d,e,str(ticket).lower()])





    except:
        sys.exit("Er is wat mis gegaan met het openen en of het schrijven van de database")


    try:
        print("Uw ticket nummer is : "+str(ticket))
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer printen.")

ticket()
