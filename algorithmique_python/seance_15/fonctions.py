from lib.functions import *

def est_pair(nombre):
    div = nombre % 2
    if div == 0 :
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")



nombre = int(input("Veuillez saisir un nombre entier : "))

est_pair(nombre)

# Correction :

def is_even(number):
    return not number%2