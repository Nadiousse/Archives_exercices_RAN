prix = float(input("Veuillez saisir le prix TTC : "))
remise = 0

if 500 <= prix <= 1000:
    remise = 2 / 100

if 1000 < prix <= 2000 :
    remise = 5 / 100

if prix > 2000 :
    remise = 10 / 100

prix_remise = prix - (prix * remise)
prix_remise = round(prix_remise, 2)

if remise == 0 :
    print("Vous n'avez pas de remise.")
else:
    print("Vous avez une remise. Total avec remise : ", prix_remise, "€.")
