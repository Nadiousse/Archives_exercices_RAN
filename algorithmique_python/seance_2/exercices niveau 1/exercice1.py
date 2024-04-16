while True:
    try:
        a = float(input("Veuillez entrer un nombre : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

while True:
    try:
        b = float(input("Veuillez entrer un nombre : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

print(a," + ", b, " = ", a+b)
print(a," - ", b, " = ", a-b)
print(a," x ", b, " = ", a*b)
print(a," / ", b, " = ", a/b)