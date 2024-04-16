départ = int(input("Veuillez saisir la borne de départ : "))
arrivée = int(input("Veuillez saisir la borne d'arrivée : "))
pas = int(input("Veuillez saisir le pas : "))

for i in range(départ, arrivée, pas):
    print(i, end=" ")