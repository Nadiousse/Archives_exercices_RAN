import math


# Fonction N°1 : double d'un nombre -> Est une fonction

def double(nombre):
    return nombre*2

# Fonction N°2 : "Bonjour + {prénom}" -> est une procédure

def hello(prenom):
    print(f"Bonjour {prenom}")

# Fonction N°3 : table de mmultiplication -> est une procédure

def table(nombre):
    for loop in range(1, 11) :
        print(loop, " x ", nombre, " = ", loop*nombre)

# Fonction N°4 : air de cercle -> est une fonction

def air_cercle(rayon):
    return rayon**2 * math.pi

# Fonction N°5 : perimètre d'un cercle -> est une fonction

def perim_cercle(rayon):
    return rayon * 2 * math.pi

# Fonction N°6 : inverse une chaîne de caractère -> procédure

def inverse_chaine(chaine):

    inverse = []
    max = len(chaine)-1

    for i in range(0, max+1):
        inverse.append(chaine[max-i])
    
    x = 0

    for i in range(0, max+1):
        print(inverse[x], end="")
        x = x + 1


#-----------------------------------------------------------------------------

# Fonction N°7 : tri d'une table numérique

def tri_table_num(table):
    z = 0
    min_table = 0
    max_table = len(table)-1
    while True:
        for i in range(min_table, max_table):
            if table[i] > table[i+1]:
                x = table[i]
                table[i] = table[i+1]
                table[i+1] = x
        for j in range(0, max_table):
            if table[i] < table[i+1]:
                z += 1
        if z == max_table-1:
            break
    print(table)

# Essai tri:

nombre_de_nombres = int(input("Veuillez saisir le nombre de chiffres du tableau : "))

tableau = []

for loop in range(nombre_de_nombres):
    tableau.append(int(input(f"Veuillez saisir le nombre numéro {loop+1}: ")))

tri_table_num(tableau)