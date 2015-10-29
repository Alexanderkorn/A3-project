__author__ = 'Stijn'


leverancier_lijst = tk.Listbox(self.leverancier_invoer_vak)

        f = ["Piet", "Jan", "Hendrik", "Hugo"]

        for i in f:
            leverancier_lijst.insert(tk.END, i)

        leverancier_lijst.place(y=200, x=135)
        def nummer_leverancier():
            goede_nummer_leverancier = str(leverancier_lijst.curselection())
            index_goede_nummer_leverancier = int(goede_nummer_leverancier[1])
            global zender_leverancier
            zender_leverancier = zenders[index_goede_nummer_leverancier]
            # aan het eind van de functie gaat hij door naar het nieuwe scherm -->
            self.Weergave_van_eigen_films()

        # je hebt een button nodig in het scherm
        # de button voort de functie hierboven uit
        verder_button = tk.Button(self.leverancier_invoer_vak, text="Verder", command=(lambda: nummer_leverancier()), font=('Verdana', 10, 'bold'))
        verder_button.place(y=380, x=130)