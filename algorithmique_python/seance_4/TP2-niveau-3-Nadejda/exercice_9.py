pointe = "_"
tige = "|"

nombre = int(input("Veuillez entrer le nombre de flèches : "))
dimention = int(input("Veuillez entrer la dimension des flèches : "))

print(pointe * nombre)

for i in range(dimention):
    print(tige * nombre)
