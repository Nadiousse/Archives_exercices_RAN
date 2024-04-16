while True:
    try:
        a = float(input("Saisissez la largeur : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

while True:
    try:
        b = float(input("Saisissez la longueur : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

while True:
    try:
        c = float(input("Saisissez la hauteur : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")


volume = a*b*c

print("Le volume du parallélépipède est ", volume, ".")