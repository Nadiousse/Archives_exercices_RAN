epaisseur_ini = int(input("Veuillez saisir l'épaisseur du papier : "))
nombre_plis = int(input("Veuillez saisir le nombre de plis : "))
epaisseur_fin = epaisseur_ini

for i in range(0,nombre_plis):
    epaisseur_fin = int(epaisseur_fin * 2)

print("L'épaisseur finale est ", epaisseur_fin, ".")