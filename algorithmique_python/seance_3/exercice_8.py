a = int(input("Veuillez saisir le nombre entier a : "))
b = int(input("Veuillez saisir le nombre entier b : "))

if a == 0 and b == 0:
    print("L'ensemblre des solutions est l'ensemble R.")

if a == 0 and b != 0:
    print("L'ensemble des solutions est l'ensemble vide.")

if a != 0 :
    ab = -b / a
    print("La solution est (-b / a), est égal à ", ab,".")