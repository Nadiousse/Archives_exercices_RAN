import random

a = int(input("Veuillez saisir un nombre entre 1 et 10 : "))

if a < 1 or a > 10 :
    print("Valeur non permise")
    a = int(input("Veuillez saisir un nombre entre 1 et 10 : "))

x = random.randrange(1,10)

while a != x :
    if a > x:
        print("Trop grand")
        a = int(input("Veuillez saisir un nombre entre 1 et 10 : "))
    if a < x:
        print("Trop petit")
        a = int(input("Veuillez saisir un nombre entre 1 et 10 : "))

if a == x:
    print("Gagné !")