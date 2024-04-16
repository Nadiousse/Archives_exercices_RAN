# Boucle allant de 1 à 10
for i in range(1, 11):
    print(i)

# Parcours d'une chaîne de caractères
mot = "Hello"
for caractere in mot: # Boucle foreach (Pour chaque)
    print(caractere)

# Parcours d'une chaine de caractère avec les indice des lettres
for i in range(0, len(mot)): # Parcours des indices
    print(f"{i} : {mot[i]}")

# BONUS !!!
# Parcours d'une chaîne de caractères à l'aide d'un Tuple
for index, lettre in enumerate(mot):
    print(f"{index} : {lettre}")