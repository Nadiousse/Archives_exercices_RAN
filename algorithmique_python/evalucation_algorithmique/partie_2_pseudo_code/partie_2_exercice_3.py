#import de Pi
import math


#definition fonction du calcul de l'aire

def calcul_aire(rayon, angle_a):
    return (math.pi * (rayon*rayon) * angle_a / 360)


#Vérification de saisie pour le rayon et l'angle


while True:
    try:
        saisi_rayon = float(input("Veuillez saisir le rayon : "))
        break
    except ValueError:
        print("Le rayon doit être un nombre à virgule ou non.", end="\n\n")
    
while True:
    try:
        saisie_angle_a = float(input("Veuillez saisir l'angle a : "))
        break
    except ValueError:
        print("Le rayon doit être un nombre à virgule ou non.", end="\n\n")

# print final avec le résultat

print(f"L'aire du cercle est de {calcul_aire(saisi_rayon, saisie_angle_a)}.")