while True:
    try:
        a = float(input("Veuillez entrer un nombre : "))
        break
    except ValueError:
        print("Erreur! Mauvais format.")


print("L'aire du carré vaut ", a*a, ".")