while True:
    try:
        a = float(input("Veuillez entrer un nombre à multiplier : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

for loop in range(1, 11) :
    print(loop, " x ", a, " = ", loop*a)