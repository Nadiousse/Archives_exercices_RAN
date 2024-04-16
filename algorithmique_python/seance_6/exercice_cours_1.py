Nb_notes = int(input("Veuillez saisir le nombre de notes : "))
total = 0

for i in range(Nb_notes):
    a = float(input("Veuillez saisir une note : "))
    total = total + a

moyenne = total / Nb_notes
moyenne = round(moyenne, 2)

print(f"La moyenne est {moyenne}/20.")