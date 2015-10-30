__author__ = 'MuscioCraft'

try:
    import csv
    import sys
    import xml.dom.minidom
    from xml.dom.minidom import parse
    from random import randint

except:
    try:
        sys.exit("Er is wat fout gegaan met importeren van de benodigde libraries.")
    except:
        print("Er is wat fout gegaan met importeren van de benodigde libraries.")



def read_xml(tag1, tag2="", tag3=None, tag4=None, tag5='film'):
#bron: http://stackoverflow.com/questions/6653128/getting-text-between-xml-tags-with-minidom
    try:
        nodes = parse('data.xml')

        #tag3(standaard 'film') zijn de tags die uit 'data.xml' worden gehaalt
        for film_nummer in nodes.getElementsByTagName(tag5):

            #magie
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

            document = film_nummer.toxml()
            dom = xml.dom.minidom.parseString(document)

            #De text tussen tag 1 wordt in text1 gezet
            text1 = handleTok(dom.getElementsByTagName(tag1))
            #De text tussen tag 2 wordt in text2 gezet
            text2 = handleTok(dom.getElementsByTagName(tag2))


            #We gebruiken dit om een tijd naast een film in de database te zetten.
            #Als het geen film is dan wordt tag4 ook niet mee gegeven als het goed is, dus dan wordt alles gepasserd
            #er wordt gekeken tag3 in text staat.
            if tag3 in text1:
                #Als tag 4 0 is dan wordt text1 gereturnd
                if tag4 == 0:
                    return text1
                #Als tag 4 1 is dan wordt text2 gereturnd
                elif tag4 == 1:
                    return text2
                elif tag4 == 2:
                    return text1, text2
                else:
                    pass
            else:
                pass

    except:
        exit("Read_xml didn't work")

def ticket():

    try:
        #Er wordt een ticket nummer aangemaakt

        ticket = randint(0,999999999)
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer aanmaken.")


    try:
        #input in variabelen zetten(In in kleine letters)
        a=str(input("Uw voornaam :")).lower()
        b=str(input("Uw achtenaam :")).lower()
        c=str(input("Uw E-mail adres :")).lower()
        #read_xml() functie gebruiken, en tag3 als input. De 0 houd in dat text1 wordt gereturnd
        d=read_xml("titel","starttijd",str(input("Welke film ? : ")), 0)
        #read_xml() functie gebruiken en tag3 als input d. De 1 houd in dat text2 wordt gereturnd
        e=read_xml("titel","starttijd",d , 1)

        #database.csv wordt geopend en de data wordt weg geschreven.
        with open('database.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', dialect='excel', lineterminator='\n')
            writer.writerow([a,b,c,d,e,str(ticket).lower()])

    except:
        sys.exit("Er is wat mis gegaan met het openen en of het schrijven van de database")


    try:
        #ticket nummer wordt terug gegeven.
        print("Uw ticket nummer is : "+str(ticket))
    except:
        sys.exit("Er is wat fout gegaan met het ticket nummer printen.")

ticket()
