x = 1
y = 0
z = "Le plus grand nombre cité est : "

print("Veuillez saisir une liste de nombres. Lorsque vous souhaitez arrêter la liste, saisissez 0.")

while x != 0:
    x = int(input("Veuillez saisir un nombre : "))
    if x > y :
        y = x

print(z, y, ".")