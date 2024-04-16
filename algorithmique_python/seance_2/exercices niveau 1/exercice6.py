while True:
    try:
        HT = float(input("Veuillez entrer le prix HT : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

taxe = 20/100
b = HT * taxe
TTC = HT + b

print("Le prix TTC est : ", TTC, ".")