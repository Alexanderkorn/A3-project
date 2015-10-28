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
    q=open('database.csv','r')
    reader=csv.reader(q, delimiter=';')
    x=0
    list2=[]
    for row in reader:
        if x == 0:
            x=1
            pass
        else:
            d = row[4]
            e = row[1]
            g = d , e
            list2.append(g)
            #list.extend(d)
    print (sorted(list2))
    #print(sorted(list, reverse=True))
    q.close()


    f=open('database.csv','r')
    reader=csv.reader(f, delimiter=';')
    x=0
    list=[]
    for row in reader:
        if x == 0:
            x=1
            pass
        else:
            b = row[4]
            a = row[1]

            c = a  , b
            list.append(c)
    print(sorted(list))

    f.close


achternamen()