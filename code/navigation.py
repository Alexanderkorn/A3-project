__author__ = 'Giuliano'

import tkinter as tk
from tkinter import *

#bron: http://stackoverflow.com/questions/6653128/getting-text-between-xml-tags-with-minidom

import xmltodict
import xml.dom.minidom
from xml.dom.minidom import parse

def read_xml():
    file = open('data.xml', 'r')
    # xml_string = file.read()
    return xmltodict.parse(xml_string)

film_nummer = None
# film_dict = read_xml()
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



from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class ThuisBioscoop(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour,
                  PageFive, PageSix, Verify1, Verify2, Verify3, Verify4,
                  Verify5, Verify6, Complete):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print(param)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        gifdir = "./"

        img = tk.PhotoImage(file=gifdir+"poster.gif")
        # tk.Button(self, image=igm).pack()


        button1 = tk.Button(self, image=img,
                            command=lambda: controller.show_frame(PageOne))
        button1.image=img
        button1.pack()

        button2 = ttk.Button(self, text="Kill Bill 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Star Wars: Episode IV",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()

        button4 = ttk.Button(self, text="Limitless",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()

        button5 = ttk.Button(self, text="007: Spectre",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()

        button6 = ttk.Button(self, text="Back to the future",
                            command=lambda: controller.show_frame(PageSix))
        button6.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The Martian", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="Kies één van de aanbieders", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        leverancier_lijst = tk.Listbox(self)
        f = ["Piet", "Jan", "Hendrik", "Hugo"]

        for i in f:
            leverancier_lijst.insert(tk.END, i)

        leverancier_lijst.pack(pady=15, padx=15)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=2, padx=2)

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame(Verify1))
        button2.pack(pady=2, padx=2)

class Verify1(tk.Frame):

    def end_choice1(self):
        print("U heeft gekozen voor The Martian")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wilt u écht naar de Martian?", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Ja",
                            command=lambda: controller.show_frame(Complete)+PageOne.end_choice1(self))
        button1.pack()

        button2 = ttk.Button(self, text="Nee",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kill Bill 2", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="Kies één van de aanbieders", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        leverancier_lijst = tk.Listbox(self)
        f = ["Piet", "Jan", "Hendrik", "Hugo"]

        for i in f:
            leverancier_lijst.insert(tk.END, i)

        leverancier_lijst.pack(pady=15, padx=15)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=2, padx=2)

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame(Verify2))
        button2.pack(pady=2, padx=2)

class Verify2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wilt u echt naar Kill Bill 2?", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Ja",
                            command=lambda: controller.show_frame(Complete))
        button1.pack()

        button2 = ttk.Button(self, text="Nee",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Star wars: Episode IV", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="Kies één van de aanbieders", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        leverancier_lijst = tk.Listbox(self)
        f = ["Piet", "Jan", "Hendrik", "Hugo"]

        for i in f:
            leverancier_lijst.insert(tk.END, i)

        leverancier_lijst.pack(pady=15, padx=15)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=2, padx=2)

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame(Verify3))
        button2.pack(pady=2, padx=2)

class Verify3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wilt u echt naar Star wars: Episode IV?", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Ja",
                            command=lambda: controller.show_frame(Complete))
        button1.pack()

        button2 = ttk.Button(self, text="Nee",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack()

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Limitless", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="Kies één van de aanbieders", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        leverancier_lijst = tk.Listbox(self)
        f = ["Piet", "Jan", "Hendrik", "Hugo"]

        for i in f:
            leverancier_lijst.insert(tk.END, i)

        leverancier_lijst.pack(pady=15, padx=15)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=2, padx=2)

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame(Verify4))
        button2.pack(pady=2, padx=2)

class Verify4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wilt u echt naar Limitless?", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Ja",
                            command=lambda: controller.show_frame(Complete))
        button1.pack()

        button2 = ttk.Button(self, text="Nee",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack()

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="007: Spectre", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="Kies één van de aanbieders", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        leverancier_lijst = tk.Listbox(self)
        f = ["Piet", "Jan", "Hendrik", "Hugo"]

        for i in f:
            leverancier_lijst.insert(tk.END, i)

        leverancier_lijst.pack(pady=15, padx=15)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=2, padx=2)

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame(Verify5))
        button2.pack(pady=2, padx=2)

class Verify5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wilt u echt naar 007: Spectre", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Ja",
                            command=lambda: controller.show_frame(Complete))
        button1.pack()

        button2 = ttk.Button(self, text="Nee",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack()

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Back to the future", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="Kies één van de aanbieders", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        leverancier_lijst = tk.Listbox(self)
        f = ["Piet", "Jan", "Hendrik", "Hugo"]

        for i in f:
            leverancier_lijst.insert(tk.END, i)

        leverancier_lijst.pack(pady=15, padx=15)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=2, padx=2)

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame(Verify6))
        button2.pack(pady=2, padx=2)

class Verify6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wilt u echt naar Back to the future?", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Ja",
                            command=lambda: controller.show_frame(Complete))
        button1.pack()

        button2 = ttk.Button(self, text="Nee",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack()

class Complete(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Uw keuze is bevestigd", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

app = ThuisBioscoop()
# print(app.filmnaam)
app.mainloop()