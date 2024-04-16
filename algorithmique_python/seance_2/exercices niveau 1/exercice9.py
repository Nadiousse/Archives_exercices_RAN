#Pas de vérification, car exercice dans le TP 3.

fr = float(input("Veuillez entrer la note de français : "))
math = float(input("Veuillez entrer la note de mathématique : "))
geom = float(input("Veuillez entrer la note de géométrie : "))
info = float(input("Veuillez entrer la note d'informatique : "))

total = fr + math + geom + info
moyenne = total / 4

print("La moyenne des notes saisies est ", moyenne,"/20.")