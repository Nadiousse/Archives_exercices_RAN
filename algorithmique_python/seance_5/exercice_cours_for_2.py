dépôt = 2000.00

taux_intérêt = 2/100

intérêt = 0

for i in range(10):
    intérêt = (dépôt * taux_intérêt)
    dépôt += intérêt

dépôt = round(dépôt, 2)

print("Dans 10 ans, vous aurez : ", dépôt, "€.")