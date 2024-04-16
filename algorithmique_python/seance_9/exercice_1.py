class PasDeNumeros(ValueError):
    pass

while True:
    try :
        saisie_texte = input("Veuillez saisir un texte : ")
        if saisie_texte.isnumeric() == True:
            raise PasDeNumeros
        break
    except PasDeNumeros:
        print("Nous vous demandons un texte. Une suite de chiffres n'est pas un texte.")

while True:
    try:
        recherche_lettre = input("Veuillez saisir la lettre recherchée : ")
        if recherche_lettre.isnumeric() == True:
            raise PasDeNumeros
        break
    except PasDeNumeros :
        print("Nous vous demandons une lettre.")

x = saisie_texte.lower().count(recherche_lettre.lower())

print(f'La lettre "{recherche_lettre}" apparait {x} fois dans le texte saisie.')