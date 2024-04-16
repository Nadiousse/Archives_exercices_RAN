while True :
    try:
        HT = float(input("Veuillez saisir le prix HT : "))
        if HT <= 0:
            print("Erreur ! Le prix doit être supérieur à 0.")
            HT = float(input("Veuillez saisir le prix HT : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

while True :
    try:
        Q = int(input("Veuillez sasir la quantité d'achat : "))
        if Q <= 0:
            print("Erreur ! La quantité doit être supérieure à 0.")
            Q = int(input("Veuillez sasir la quantité d'achat : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

while True :
    try:
        a = float(input("Veuillez sasir le pourcentage de TVA (sans le %) : "))
        if 0 < a <= 100:
            print("Erreur ! Le pourcentage doit être comprit entre 0 et 100.")
            a = float(input("Veuillez sasir le pourcentage de TVA (sans le %) : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")


TVA = a/100
remise = 15/100

prix_sans_tva_sans_remise = HT * Q
montant_remise = prix_sans_tva_sans_remise * remise
prix_sans_tva_avec_remise = prix_sans_tva_sans_remise - montant_remise
montant_tva = prix_sans_tva_avec_remise * TVA
TTC = prix_sans_tva_avec_remise + montant_tva

print("Le total est de ", TTC, "€ TTC.")