while True:
    try:
        main_a = int(input("Nombre de doigts de la main A : "))
        if main_a < 0 or main_a > 5:
            raise ValueError
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

while True:
    try:
        main_b = int(input("Nombre de doigts de la main B : "))
        if main_b < 0 or main_b > 5:
            raise ValueError
        break
    except ValueError:
        print("Erreur ! Mauvais format.")


total = main_a + main_b

modulo = total % 2

if modulo == 0 :
    print("A a gagné.")
else:
    print("B a gagné.")