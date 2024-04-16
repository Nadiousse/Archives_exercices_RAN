#Définition de la fonction qui calcul le pourcentage de perte

def pourcentage_de_perte(prix):
    perte = prix * 0.07
    return (perte)


#Variables

prix_voiture = 0.00
annee_de_vente = 0
annee_actuelle = 2023
nb_annees_entre_achat_vente = 0
nb_pertes = 0


# Vérification de la saisie du prix de la voiture

while True:
    try:
        prix_voiture = float(input("Veuillez saisir le prix d'achat de la voiture : "))
        break
    except ValueError:
        print("Mauvais format !", end="\n\n")


# Vérification de la saisie de l'année de vente

while True:
    try:
        annee_de_vente = int(input("Veuillez entrer l'année de vente envisagé : "))

        if annee_de_vente < annee_actuelle:
            raise Exception
        
        break
    except ValueError:
        print(f"Mauvais format ! L'année de vente ne peut être inférieure à l'année en cours ({annee_actuelle})")

# Calcul du nombre d'années entre l'année d'achat et l'année de revente

nb_annees_entre_achat_vente = annee_de_vente - annee_actuelle

# Calcul du prix de revente

prix_revente = prix_voiture #Prix de revente commence par le prix de la voiture

while nb_pertes != nb_annees_entre_achat_vente:
    prix_revente -= pourcentage_de_perte(prix_revente) #Prix de revente baisse à chaque année par 7% de la valeur de la voiture à partir du prix de l'année précédente
    nb_pertes += 1

# Print final avec le résultat de calcul

print(f"Le prix de revente de la voiture en {annee_de_vente} sera de {prix_revente}€.")