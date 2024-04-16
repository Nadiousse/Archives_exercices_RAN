class PasDeNumeros(ValueError):
    pass

NbMax = 0
y = "x"

while True:
    try :
        saisie_texte = input("Veuillez saisir un texte : ")
        if saisie_texte.isnumeric() == True:
            raise PasDeNumeros
        break
    except PasDeNumeros:
        print("Nous vous demandons un texte. Une suite de chiffres n'est pas un texte.")

for lettre in saisie_texte:
    if lettre == "é":
        saisie_texte = saisie_texte.replace("é", "e")
    if lettre == "è":
        saisie_texte = saisie_texte.replace("è", "e")
    if lettre == "ê":
        saisie_texte = saisie_texte.replace("ê", "e")

print(saisie_texte)

saisie_texte_sans_espace = saisie_texte.replace(" ", "") 

for lettre in saisie_texte_sans_espace:
    x = saisie_texte_sans_espace.lower().count(lettre)
    if x > NbMax :
        NbMax = x
        y = lettre

print(f'La lettre {y} est la plus présente dans le texte. Avec {NbMax} récurences.')