__author__ = 'alexander'
print('Hello world')


Treintraject = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum' ,'Zaandam','Amsterdam Sloterdijk', 'Amsterdam Centraal',
'Amsterdam Amstel','Utrecht Centraal','s-Hertogenbosch','Eindhoven','Weert','Roermond','Sittard','Maastricht']

for i in range (len(Treintraject)):
    for j in range(i+1, len(Treintraject)):
        print("Het huidige station is: " + Treintraject[i])
        print("De resterende stations zijn: "+ str(Treintraject[j:]))
        break
    if i+1 == len(Treintraject):
        print("Het huidige station is: Maastricht")
        print("Dit is het eindpunt")
#    else:
#        print("Het huidige station is: " + str(Treintraject[i]))
#        print("De resterende stations zijn: " + str(Treintraject[i+1:len(Treintraject)]))

#hoi