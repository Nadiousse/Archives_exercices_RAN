#Pas de vérification, car exercice dans le TP3.


francais_note = float(input("Veuillez saisir la note de français : "))
francais_coef = float(input("Veuillez saisir le coefficient de français : "))
moyenne_francais = francais_note * francais_coef

maths_note = float(input("Veuillez saisir la note de maths : "))
maths_coef = float(input("Veuillez saisir le coefficient de maths : "))
moyenne_maths = maths_note * maths_coef

geometrie_note = float(input("Veuillez saisir la note de géomètrie : "))
geometrie_coef = float(input("Veuillez saisir le coefficient de géomètrie : "))
moyenne_geometrie = geometrie_note * geometrie_coef

informatique_note = float(input("Veuillez saisir la note d'informatique : "))
informatique_coef = float(input("Veuillez saisir le coefficient d'informatique : "))
moyenne_informatique = informatique_note * informatique_coef

total_notes = moyenne_francais + moyenne_geometrie + moyenne_informatique + moyenne_maths
division = francais_coef + maths_coef + geometrie_coef + informatique_coef

moyenne = round(total_notes / division, 2)

print("La moyenne est de ", moyenne, ".")

