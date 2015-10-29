__author__ = 'Stijn'
import tkinter as tk

win = tk.Tk()
leverancier_lijst = tk.Listbox(win)
leverancier_lijst.place(y=200, x=135)

f = ["Piet", "Jan", "Hendrik", "Hugo"]

for i in f:
    leverancier_lijst.insert(tk.END, i)

# def nummer_leverancier():
#     goede_nummer_leverancier = str(leverancier_lijst.curselection())
#     index_goede_nummer_leverancier = int(goede_nummer_leverancier[1])
#     global zender_leverancier
#     zender_leverancier = zenders[index_goede_nummer_leverancier]
#     # aan het eind van de functie gaat hij door naar het nieuwe scherm -->
#     self.Weergave_van_eigen_films()

# je hebt een button nodig in het scherm
# de button voort de functie hierboven uit
verder_button = tk.Button(win, text="Verder", command=(lambda: None), font=('Verdana', 10, 'bold'))
verder_button.place(y=380, x=130)

win.mainloop()