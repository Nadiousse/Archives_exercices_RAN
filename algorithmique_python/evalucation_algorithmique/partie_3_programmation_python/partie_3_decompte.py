#Définition des variables:

Nom = ""
NbNom = 0

#Saisie jusqu'à arrêt avec le terme "fin"

while Nom != "fin":
    Nom = input(f"Veuillez saisir le nom numéro {NbNom+1}. Pour arrêter la saisie, entrer 'fin' : ")
    NbNom += 1
    

#Print de fin avec le nombre total de noms saisis :

print(f"Vous avez saisi {NbNom-1} noms.")