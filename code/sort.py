__author__ = 'Roy'
from xml.dom.minidom import parse

import xmltodict


def read_xml():
    file = open('data.xml','r')
    xml_string = file.read()
    return xmltodict.parse(xml_string)

film_nummer = None
film_dict = read_xml()
nodes = parse('data.xml')
for film_nummer in nodes.getElementsByTagName('film'): # 7 = in range of childnodes
    #print(film_dict['filmsoptv']['film'][film_nummer]['starttijd'])
    print(film_nummer.toxml())

