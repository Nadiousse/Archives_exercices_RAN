
matière = ["français", "maths", "géographie", "l'informatique"]
notes = [0, 0, 0, 0]
coefs = [0, 0, 0, 0]
appréciation = ["Nul", "Insuffisant", "Assez bien", "Bien", "Très bien"]

total = 0
moyenne = 0
division = 0

for i in range(4):

    x = "Veuillez entrer la note de " + matière[i] + " : "

    notes[i] = float(input(x))
    while notes[i] < 0 or notes[i] > 20 :
        print("Merci de rentrer un nombre entre 0 et 20.")
        notes[i] = float(input(x))

    y = "Veuillez entrer le coéfficient de " + matière[i] + " : "

    coefs[i] = float(input(y))
    while coefs[i] < 1 or coefs[i] > 10 :
        print("Merci de rentrer un nombre entre 1 et 10.")
        coefs[i] = float(input(y))

for i in range(4):
    total = total + (notes[i] * coefs[i])
    division = division + coefs[i]

moyenne = total / division
moyenne = round(moyenne, 2)

if moyenne <=4 :
    a = 0
elif 4 < moyenne <= 8:
    a = 1
elif 8 < moyenne <= 12:
    a = 2
elif 12 < moyenne <= 16 :
    a = 3
else:
    a = 4

print("La moyenne générale est de ", moyenne, "/20. C'est ", appréciation[a], " !")