# Listes :

matières = []
prénoms = []
noms = []
liste_notes = []
moyennes = []
moyennes_matières = []
listes_note_eleves = []

# Variables :

nb_matières = 1
nb_élèves = 1
total_notes = 0
moyenne = 0

# Etape 1 : saisir le nombre et les noms des matières.

while True :
    try :
        nb_matières = int(input("Veuillez saisir le nombre de matières : "))
        break
    except ValueError:
        print("Mauvais format ! Veuillez saisir un nombre entier.")

# Etape 2 : saisir les matières.

for i in range(nb_matières):
    matières.append(input("Veuillez saisir une matière : "))

# Etape 3 : saisir le nombre d'élèves.

while True :
    try :
        nb_élèves = int(input("Veuillez saisir le nombre d'élèves : "))
        break
    except ValueError:
        print("Mauvais format ! Veuillez saisir un nombre entier.")

# Etape 4 : saisir les prénoms et les noms des élèves.

for j in range(nb_élèves):
    prénoms.append(input(f"Veuillez entrer le prénom de l'élève {i} :"))
    noms.append(input(f"Veuillez entrer le nom de l'élève {i} :"))

# Etape 5 : saisir les notes par matière.

for m in range(nb_élèves):
    liste_notes.append(0)

for m in range(nb_matières):
    moyennes_matières.append(0)

for k in range(nb_élèves):
    listes_note_eleves.append(f"{prénoms[k]} {noms[k]} : \n ----------------------- \n")
    for l in range(nb_matières):
        while True :
            try:
                liste_notes[l] = float(input(f"Veuillez saisir la note de {matières[l]} de {prénoms[k]} {noms[k]} :"))
                listes_note_eleves[k] += f"{matières[l]} : {liste_notes[l]}/20 \n"
                moyennes_matières[l] += liste_notes[l]
                total_notes += liste_notes[l]
                break
            except ValueError:
                print("Erreur ! Veuillez saisir un nombre.")
    moyennes.append(total_notes / nb_matières)
    listes_note_eleves[k] += f"Avec une moyenne générale de {moyennes[k]}/20. \n ----------------------- \n"
    total_notes = 0

for n in range(nb_élèves):
    print(listes_note_eleves[n])

# Etape 6 : print les moyennes par matières.

for i in range(nb_matières):
    moyennes_matières[i] = moyennes_matières[i] / nb_élèves
    print(f"La moyenne de la classe pour la matière {matières[i]} est de {moyennes_matières[i]}/20.")

# Etape 7 : le pire et le meilleur élève

max_moyenne = 0
max_index = 0
min_moyenne = 21
min_index = 0
x = 0

for i in range(0, len(moyennes)):
    x = moyennes[i]
    if x < min_moyenne:
        min_moyenne = x
        min_index = i
    if x > max_moyenne:
        max_moyenne = x
        max_index = i

print(f"Le meilleur élève de la classe est {prénoms[max_index]} {noms[max_index]} avec une moyenne de {moyennes[max_index]}/20.")
print(f"Le pire élève de la classe est {prénoms[min_index]} {noms[min_index]} avec une moyenne de {moyennes[min_index]}/20.")