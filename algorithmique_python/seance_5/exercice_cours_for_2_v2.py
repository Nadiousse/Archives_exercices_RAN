dépôt = float(input("Veuillez saisir le dépôt initial : "))

taux = float(input("Veuillez saisir le pourcentage d'intérêts (sans le %) : "))

taux_intérêt = taux / 100

intérêt = 0

for i in range(10):
    intérêt = (dépôt * taux_intérêt)
    dépôt += intérêt

dépôt = round(dépôt, 2)

print("Dans 10 ans, vous aurez : ", dépôt, "€.")