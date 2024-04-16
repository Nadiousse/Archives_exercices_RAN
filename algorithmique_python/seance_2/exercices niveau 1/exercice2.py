while True:
    try:
        a = float(input("Veuillez entrer un nombre : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

print("Le double de ce nombre vaut : ", a*2, ".")