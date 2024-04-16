x = 0
y = 0
z = "Le plus grand nombre cité parmi les 20 est : "

for i in range(20):
    x = int(input("Veuillez saisir un nombre : "))
    if x > y :
        y = x

print(z, y, ".")