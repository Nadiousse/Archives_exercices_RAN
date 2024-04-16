while True:
    try:
        x = int(input("Veuillez saisir un nombre allant de -1000 à 1000 : "))
        break
    except ValueError:
        print("Mauvais format.")


if x == 0:
    print("Le nombre est nul.")
    
if x > 0:
    print("Le nombre est positif.")

if x < 0:
    print("Le nombre est négatif.")