Mentions = ["Nul", "Insuffisant", "Assez bien", "Bien", "Très bien"]

francais = float(input("Veuillez saisir la note de français : "))
maths = float(input("Veuillez saisir la note des mathématiques : "))
geo = float(input("Veuillez saisir la note de géographie : "))
info = float(input("Veuillez saisir la note de l'informatique : "))

moyenne = (francais + maths + geo + info) / 4
moyenne = round(moyenne, 2)

mention = 0

if 4 <= moyenne <= 8 :
    mention = 1

if 8 < moyenne <= 12 :
    mention = 2

if 12 < moyenne <= 16 :
    mention = 3

if 16 < moyenne <= 20 :
    mention = 4


print ("Votre moyenne est ", moyenne,", alors vous avez la mention ", Mentions[mention], ".")