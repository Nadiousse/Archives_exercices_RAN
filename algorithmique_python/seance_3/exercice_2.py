while True:
    try:
        x = int(input("Veuillez saisir un nombre entier : "))
        break
    except ValueError:
        print("Erreur! Mauvais format.")

while True:
    try:
        y = int(input("Veuillez saisir un nombre entier : "))
        break
    except ValueError:
        print("Erreur! Mauvais format.")

while True:
    try:
        z = int(input("Veuillez saisir un nombre entier : "))
        break
    except ValueError:
        print("Erreur! Mauvais format.")

if x < y < z :
    print("Les nombre ont été saisis dans l'ordre croissant.")
else:
    print("Les nombre n'ont pas été saisis dans l'ordre croissant.")