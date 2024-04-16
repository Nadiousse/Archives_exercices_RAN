HT = float(input("Veuillez saisir le prix hors taxe : "))

TVA_liste = [0, 5.5, 19.6, 33]

x = int(input("Pour une tva de 5.5%, saisissez 1. \nPour une tva de 19.6%, saisissez 2. \nPour une tva de 33%, saisissez 3. "))

tva = HT * TVA_liste[x] / 100
prix = HT + tva

print("Le prix HT est de ", HT,"€, la TVA est de ", TVA_liste[x], "% et le prix TTC est de ", prix,".")