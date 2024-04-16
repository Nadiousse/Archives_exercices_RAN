
#Variables:
pourcent_remise = 0.05 # 5/100 = 5% de remise
remise = 0
total_sans_remise = 0
total_avec_remise = 0


# Vérification de la saisie du prix en float:
while True:
    try :
        prix_produit = float(input("Veuillez saisir le prix du produit à l'unité : "))
        print("")
        break
    except ValueError:
        print("Le prix n'est dans le bon format.", end="\n\n")


#Vérification de la saisie du nombre de produits en int:
while True:
    try:
        nombre_de_produits = int(input("Veuillez saisir la quantité acheté : "))
        print("")
        break
    except ValueError:
        print("La quantité doit être un nombre entier.", end="\n\n")


# Calculs du montant total :

total_sans_remise = prix_produit * nombre_de_produits # calcul du montant sans remise

remise = total_sans_remise * pourcent_remise  #calcul du montant de la remise

total_avec_remise = total_sans_remise - remise # calcul du montant après remise


# Print du total obtenu:

print(f"Le prix total avec remise est de {total_avec_remise}€.")