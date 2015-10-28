__author__ = 'Roy'
#bron: http://stackoverflow.com/questions/6653128/getting-text-between-xml-tags-with-minidom

import xmltodict
import xml.dom.minidom
import csv
from xml.dom.minidom import parse

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
    foo = dom.getElementsByTagName("starttijd")
    text = handleTok(foo)

    bob = dom.getElementsByTagName("titel")
    text2 = handleTok(bob)
    print(text, text2)




def achternamen():
    f=open('database.csv','r')
    reader=csv.reader(f, delimiter=';')
    x=0
    for row in reader:
        if x == 0:
            x=1
            pass
        else:
            a = row[1]
            print(sorted(a))

    f.close()

achternamen()

