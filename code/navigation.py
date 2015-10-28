__author__ = 'Giuliano'

import tkinter as tk
#bron: http://stackoverflow.com/questions/6653128/getting-text-between-xml-tags-with-minidom

import xmltodict
import xml.dom.minidom
from xml.dom.minidom import parse

def read_xml():
    file = open('data.xml', 'r')
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

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix):

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
        poster1 = tk.PhotoImage(file=gifdir+"poster.gif")

        button1 = ttk.Button(self, text="The Martian", image=poster1,
                            command=lambda: controller.show_frame(PageOne))
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

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame())
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kill Bill 2", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame())
        button2.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Star wars: Episode IV", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        self.button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame())
        button2.pack()

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Limitless", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame())
        button2.pack()

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="007: Spectre", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame())
        button2.pack()

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Back to the future", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Terug naar home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Inschrijven",
                             command=lambda: controller.show_frame())
        button2.pack()

app = ThuisBioscoop()
# print(app.filmnaam)
app.mainloop()