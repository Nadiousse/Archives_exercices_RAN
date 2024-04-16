nombre = int(input("Saisissez un nombre : "))
quotient = nombre
binaire = []
inverse = []

while quotient != 0 :
    reste = quotient % 2
    if reste == 1:
        binaire.append(1)
    else:
        binaire.append(0)
    quotient = quotient // 2

total = len(binaire)
max = total - 1

for i in range(0, total):
    inverse.append(binaire[max-i])

liste_string = f'{inverse}'
binaire_texte = ""
x = 0

print("En binaire : ", end="")

x = 0

for i in range(0, total):
    print(inverse[x], end="")
    x = x + 1